import os
import thread
import time
from datetime import datetime

def time_thread(delay, duracao):
	tempo_inicio = datetime.now().time()
	acabou_hora = tempo_inicio.hour + duracao.hour
	acabou_minutos = tempo_inicio.minute + duracao.minute
	acabou_segundos = tempo_inicio.second + duracao.second

	while 1:
		tempo_atual = datetime.now().time()
		
		if tempo_atual.hour == acabou_hora and tempo_atual.minute == acabou_minutos and tempo_atual.second == acabou_segundos:
			print("acabou")
			thread.exit()					

		print("not yet")
		time.sleep(delay)
	return

def provas_dinamica():
	provaId = session.dinamica
	row = db(db.provasd.cod_prova == provaId, db.provasd.ALL).select().first()
	dif_inicio = row.dif_inicio

	if session.questaoIds == None:
		questao = db(db.questoes.dificuldade == dif_inicio, db.questoes.ALL).select(orderby='<random>').first()
		session.questaoIds = questao.id
	else:
		questao = db(db.questoes.id == session.questaoIds, db.questoes.ALL).select().first()

	fields = []
	labels = {}


	dicionario = {}	
	labels.update({"questao" + str(1): str(1) + ") " + questao.enunciado})
	dicionario.update({"certo":questao.resposta, "errado1":questao.resp1, "errado2":questao.resp2, "errado3":questao.resp3})
	field = Field('questao' + str(1), requires=IS_IN_SET(dicionario), widget=SQLFORM.widgets.radio.widget)
	fields.append(field)

	form = SQLFORM.factory(*fields, labels=labels)

	if form.accepts(request.vars, session):
		if form.vars.values()[0] == "certo":
			session.acerto = 1
			session.dif_proxima = questao.acerto_goto
		else:
			session.acerto = 0
			session.dif_proxima = questao.erro_goto

		redirect(URL('provas', 'proxima_questao'))

	return dict(form=form)

def proxima_questao():
	provaId = session.dinamica
	row = db(db.provasd.cod_prova==provaId, db.provasd.ALL).select().first()
	dif = session.dif_proxima
	if session.prox_questao == None:
		questao = db(db.questoes.dificuldade == dif, db.questoes.ALL).select(orderby='<random>').first()
		session.prox_questao = questao.id
	else:
		questao = db(db.questoes.id == session.prox_questao, db.questoes.ALL).select().first()

	fields = []
	labels = {}

	dicionario = {}	
	labels.update({"questao" + str(1): str(1) + ") " + questao.enunciado})
	dicionario.update({"certo":questao.resposta, "errado1":questao.resp1, "errado2":questao.resp2, "errado3":questao.resp3})
	field = Field('questao' + str(1), requires=IS_IN_SET(dicionario), widget=SQLFORM.widgets.radio.widget)
	fields.append(field)

	form = SQLFORM.factory(*fields, labels=labels)

	if form.accepts(request.vars, session):
		if form.vars.values()[0] == "certo":
			session.acerto += 1

		nota = 0
		acertos = session.acerto
		nota_por_acerto = float(10.00/float(2))

		nota = float(acertos) * nota_por_acerto
		user_prof = row.user_prof
		user_aluno = session.user_aluno
		cod_prova = session.dinamica

		prova_upload_to_insert = {'user_prof':user_prof, 'user_aluno':user_aluno, 'nota':nota, 'cod_prova':cod_prova}
		db.provas_uploads.insert(**prova_upload_to_insert)

		redirect(URL('controlesaluno', 'home'))			

	return dict(form=form)

def provas_estatica():
	provaId = session.estatica
	row = db(db.provase.cod_prova==provaId, db.provase.ALL).select().first()
	total = row.total
	questoes = row.cod_questoes.split(',')
	fields = []
	labels = {}

	for i in range(len(questoes)):
		dicionario = {}
		questao = db(db.questoes.id==int(questoes[i]), db.questoes.ALL).select().first()
		labels.update({"questao" + str(i+1): str(i+1) + ") " + questao.enunciado})
		dicionario.update({"certo":questao.resposta, "errado1":questao.resp1, "errado2":questao.resp2, "errado3":questao.resp3})
		field = Field('questao' + str(i+1), requires=IS_IN_SET(dicionario), widget=SQLFORM.widgets.radio.widget)
		fields.append(field)

	form = SQLFORM.factory(*fields, labels=labels)
	
	duracao = row.tempo	

	try:
		thread.start_new_thread( time_thread, (1, duracao))
	except:
		print "Error: unable to start thread"

	if form.accepts(request.vars, session):		
		nota = 0
		acertos = 0
		nota_por_acerto = float(10.00/float(total))
		for i in range(len(form.vars)):
			if form.vars.values()[i] == "certo":				
				acertos += 1

		nota = float(acertos) * nota_por_acerto
		user_prof = row.user_prof
		user_aluno = session.user_aluno
		cod_prova = provaId

		prova_upload_to_insert = {'user_prof':user_prof, 'user_aluno':user_aluno, 'nota':nota, 'cod_prova':cod_prova}
		db.provas_uploads.insert(**prova_upload_to_insert)

		redirect(URL('provas', 'feedback_estatica'))

	return dict(form=form)

def feedback_estatica():
	provaId = session.estatica
	row = db(db.provase.cod_prova==provaId, db.provase.ALL).select().first()
	questoes = row.cod_questoes.split(',')

	divs = create_feedback_view(questoes)	
	return {"divs" : XML(divs)}

def create_feedback_view(questoes):
	divs = "<table><thead><tr><th>Questão</th><th>Resposta 1 <span>(Correta)</span></th><th>Feedback 1</th><th>Resposta 2</th><th>Feedback 2</th>"
	divs += "<th>Resposta 3</th><th>Feedback 3</th><th>Resposta 4</th><th>Feedback 4</th></tr></thead><tbody>"	
	for i in range(len(questoes)):
		questao = db(db.questoes.id==int(questoes[i]), db.questoes.ALL).select().first()
		divs += "<tr><td>" + str(i+1) + "</td><td>" + questao.resposta + "</td><td>" + questao.feed_resp + "</td><td>" + questao.resp1 + "</td>"
		divs += "<td>" + questao.feed_r1 + "</td><td>" + questao.resp2 + "</td><td>" + questao.feed_r2 + "</td><td>" + questao.resp3 + "</td><td>" + questao.feed_r3+ "</td></tr>"

	return divs
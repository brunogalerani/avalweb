import os

def provas_dinamica():

	return dict()

def provas_estatica():
	provaId = session.estatica
	row = db(db.provase.id==provaId, db.provase.ALL).select().first()
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

	if form.accepts(request.vars, session):		
		nota = 0
		acertos = 0
		nota_por_acerto = float(10.00/float(total))
		for i in range(len(form.vars)):
			print("Entrou " + str(i))
			if form.vars.values()[i] == "certo":				
				acertos += 1

		nota = float(acertos) * nota_por_acerto
		user_prof = row.user_prof
		user_aluno = session.user_aluno
		cod_prova = provaId

		prova_upload_to_insert = {'user_prof':user_prof, 'user_aluno':user_aluno, 'nota':nota, 'cod_prova':cod_prova}
		db.provas_uploads.insert(**prova_upload_to_insert)

		print('acertos= ' + str(acertos) + " nota_por_acerto=" + str(nota_por_acerto))

		redirect(URL('provas', 'feedback_estatica'))

	return dict(form=form)

def feedback_estatica():
	provaId = session.estatica
	row = db(db.provase.id==provaId, db.provase.ALL).select().first()
	questoes = row.cod_questoes.split(',')
	divs = ""	
	for i in range(len(questoes)):
		questao = db(db.questoes.id==int(questoes[i]), db.questoes.ALL).select().first()
		divs += '<div style="display:inline-block; margin-right: 150px; margin-bottom: 50px;"><p style="margin-left:20px;">Questão ' + str(i+1) + "</p>" 
		divs += "<ul><li style='color:green;'> Resposta 1:<br> " + questao.resposta + "</li>" + "<li>Feedback:<br>" + questao.feed_resp + "</li></ul>" 
		divs += "<ul><li style='color:red;'>Resposta 2:<br>" + questao.resp1 + "</li>" + "<li>Feedback:<br>" + questao.feed_r1 + "</li></ul>" 
		divs += "<ul><li style='color:red;'>Resposta 3:<br>" + questao.resp2 + "</li>" + "<li>Feedback:<br>" + questao.feed_r2 + "</li></ul>" 
		divs += "<ul><li style='color:red;'>Resposta 4:<br>" + questao.resp3 + "</li>" + "<li>Feedback:<br>" + questao.feed_r3 + "</li></ul></div>"
	
	return {"divs" : XML(divs)}
dificuldades = ('Fácil', 'Médio', 'Difícil')

def questao():
	labels = {'topic_name':'Disciplina', 'user_prof':'Professor', 'video_enunc':'Imagem Enunciado', 'resposta':'Resposta Correta', 
	'resp1':'Resposta 1', 'resp2':'Resposta 2', 'resp3':'Resposta3', 'feed_resp':'Feedback Resposta Correta', 'feed_r1':'Feedback Resposta 1', 
	'feed_r2':'Feedback Resposta 2', 'feed_r3':'Feedback Resposta 3', 'acerto_goto':'Dificuldade se acertar', 'erro_goto':'Dificuldade se errar',
	'topic':'Assunto', 'parte':'Parte do conteúdo'}

	form = SQLFORM.factory(	
	Field('topic_name', requires=IS_NOT_EMPTY()),	
	Field('enunciado', 'text', requires=IS_NOT_EMPTY()),
	Field('video_enunc', 'upload', default='', requires=IS_NOT_EMPTY()),
	Field('resposta', 'text', requires=IS_NOT_EMPTY()),
	Field('resp1', 'text', requires=IS_NOT_EMPTY()),
	Field('resp2', 'text', requires=IS_NOT_EMPTY()),
	Field('resp3', 'text', requires=IS_NOT_EMPTY()),
	Field('feed_resp', 'text', requires=IS_NOT_EMPTY()),
	Field('feed_r1', 'text', requires=IS_NOT_EMPTY()),
	Field('feed_r2', 'text', requires=IS_NOT_EMPTY()),
	Field('feed_r3', requires=IS_NOT_EMPTY()),
	Field('dificuldade', requires=(IS_IN_SET(dificuldades))),
	Field('acerto_goto', requires=IS_IN_SET(dificuldades)),
	Field('erro_goto', requires=IS_IN_SET(dificuldades)),
	Field('topic', 'text', requires=IS_NOT_EMPTY()),
	Field('parte', 'text', requires=IS_NOT_EMPTY()),
	labels = labels,
	submit_button = "Criar")
	form.vars.user_prof = session.user_prof
	if form.process(session=None, formname='test').accepted:
		db.questoes.insert(**form.vars)
		response.flash=T("Questão cadastrada com sucesso!")

	return dict(form=form)

def provae():
	labels = {'total':'Total de Questões', 'tempo':'Tempo', 'topic_name':'Disciplina', 'parte':'Parte do Conteúdo', 'aval':'Tipo da Prova'}

	form = SQLFORM.factory(
    Field('tempo', 'time', requires=IS_NOT_EMPTY()),
    Field('topic_name', requires=IS_NOT_EMPTY()),
    Field('parte', requires=IS_NOT_EMPTY()),
    Field('aval', requires=IS_NOT_EMPTY()),
    Field('total', requires=IS_NOT_EMPTY()),
	labels = labels,
	submit_button = "Criar")

	form.vars.user_prof = session.user_prof
	if form.process(session=None, formname='test').accepted:
		db.provas.insert(**{'user_prof' : session.user_prof, 'topic_name' : form.vars.topic_name, 'modo_prova' : 'estatica' ,'aval' : form.vars.aval})
		provaId = db().select(db.provas.id).last()
		dicionario = form.vars.copy()

		questao = ''
		for i in range(1, int(request.vars.total) + 1):
			questao += request.vars[str(i)] + ","

		questao = questao[:-1]
		dicionario.update({'cod_questoes':questao, 'cod_prova': provaId})
		db.provase.insert(**dicionario)
		response.flash=T("Prova Cadastrada com Sucesso! ")

	return dict(form=form)

def provad():
	labels = {'num_total':'Total de Questões', 'tempo':'Tempo', 'dif_inicio':'Dificuldade Inicial', 'topic_name':'Disciplina', 'parte':'Parte do Conteúdo', 'aval':'Tipo da Prova'}

	form = SQLFORM.factory(		
		Field('tempo', 'time', requires=IS_NOT_EMPTY()),
		Field('dificuldade', requires=(IS_IN_SET(dificuldades))),
		Field('dif_inicio', requires=(IS_IN_SET(dificuldades))),
		Field('topic_name', requires=IS_NOT_EMPTY()),
		Field('parte', requires=IS_NOT_EMPTY()),
		Field('aval', requires=IS_NOT_EMPTY()),
		Field('num_total', 'integer', requires=IS_NOT_EMPTY()),
		labels = labels,
		submit_button = "Criar")

	form.vars.user_prof = session.user_prof
	if form.process(session=None, formname='test').accepted:
		db.provas.insert(**{'user_prof' : session.user_prof, 'topic_name' : form.vars.topic_name, 'modo_prova' : 'dinamica' ,'aval' : form.vars.aval})
		provaId = db().select(db.provas.id).last()
		dicionario = form.vars.copy()
		dicionario.update({'cod_prova': provaId})
		db.provasd.insert(**dicionario)
		response.flash=T("Prova Cadastrada com Sucesso! ")

	return dict(form=form)
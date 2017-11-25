def questao():
	labels = {'topic_name':'Disciplina', 'user_prof':'Professor', 'video_enunc':'Imagem Enunciado', 'resposta':'Resposta Correta', 
	'resp1':'Resposta 1', 'resp2':'Resposta 2', 'resp3':'Resposta3', 'feed_resp':'Feedback Resposta Correta', 'feed_r1':'Feedback Resposta 1', 
	'feed_r2':'Feedback Resposta 2', 'feed_r3':'Feedback Resposta 3', 'acerto_goto':'Dificuldade se acertar', 'erro_goto':'Dificuldade se errar',
	'topic':'Assunto', 'parte':'Parte do conteúdo'}
	
	dificuldades = ('Fácil', 'Médio', 'Difícil')

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
	labels = labels)
	form.vars.user_prof = session.user_prof
	if form.process(session=None, formname='test').accepted:
		db.questoes.insert(**form.vars)
		response.flash=T("Questão cadastrada com sucesso!")

	return dict(form=form)
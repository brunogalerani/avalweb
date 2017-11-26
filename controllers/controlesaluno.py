def home():
	labels = {'cod_prova':'Código da Prova'}

	form = SQLFORM.factory(
		Field('cod_prova', 'integer', requires=IS_NOT_EMPTY()),
		labels = labels,
		submit_button = 'Encontrar prova!'
	)

	ja_fez = False

	if form.process().accepted:
		for row in db().select(db.provasd.cod_prova):			
			if row.cod_prova == int(form.vars.cod_prova):
				for item in db(db.provas_uploads.cod_prova==row.cod_prova, db.provas_uploads.ALL).select():
					if item.user_aluno == session.user_aluno:						
						ja_fez = True
						break
				if ja_fez:
					session.dinamica = row.cod_prova
					if session.questaoIds:
						session.questaoIds = None
						session.endDinamica = None
						session.questoesRespondidas = []
						session.acertos = 0
					redirect(URL('provas', 'provas_dinamica'))
					break

		for row2 in db().select(db.provase.cod_prova):			
			if row2.cod_prova == int(form.vars.cod_prova):
				for item in db(db.provas_uploads.cod_prova==row2.cod_prova, db.provas_uploads.ALL).select():
					if item.user_aluno == session.user_aluno:
						ja_fez = True
						break
				if not ja_fez:
					session.estatica = row2.cod_prova
					redirect(URL('provas', 'provas_estatica'))
					break
					
		mensagem_final =  "Código inválido" if not ja_fez else "Este aluno já realizou esta prova!"
		response.flash=T(mensagem_final)
	return dict(form=form)

def ver_notas():
	return dict()
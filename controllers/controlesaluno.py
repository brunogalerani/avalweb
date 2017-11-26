def home():
	labels = {'cod_prova':'Código da Prova'}

	form = SQLFORM.factory(
		Field('cod_prova', 'integer', requires=IS_NOT_EMPTY()),
		labels = labels,
		submit_button = 'Encontrar prova!'
	)

	if form.process().accepted:
		for row in db().select(db.provasd.cod_prova):			
			if row.cod_prova == int(form.vars.cod_prova):
				redirect(URL('provas', 'provas_dinamica'))
				break

		for row2 in db().select(db.provase.cod_prova):			
			if row2.cod_prova == int(form.vars.cod_prova):
				redirect(URL('provas', 'provas_estatica'))
				break

		response.flash=T("Código inválido!")
	return dict(form=form)
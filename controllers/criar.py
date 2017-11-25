def questao():
	form = SQLFORM(db.questoes)
	if form.process(session=None, formname='test').accepted:
		response.flash = 'form accepted'
	return dict(form=form)
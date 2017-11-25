def aluno():
	try:
		labels = {'user_aluno':'Usuário', 'passw_aluno':'Senha', 'nome_aluno':'Nome completo', 'email_aluno':'E-mail'}
		form = SQLFORM(db.aluno, 
			submit_button='Cadastrar', 
			labels = labels, 
			length=100)   
		if form.accepts(request.vars, session):
			response.flash = 'Cadastrado com sucesso'
	except Exception:
		response.flash = 'Usuário já cadastrado'
	return dict(form=form)
    
def professor():
	try:
		labels = {'user_prof':'Usuário', 'passw_prof':'Senha', 'nome_prof':'Nome completo', 'email_prof':'E-mail'}
		form = SQLFORM(db.professor, 
			submit_button='Cadastrar', 
			labels = labels, 
			length=100)   
		if form.accepts(request.vars, session):
			response.flash = 'Cadastrado com sucesso'
	except Exception:
		response.flash = 'Usuário já cadastrado'
	return dict(form=form)
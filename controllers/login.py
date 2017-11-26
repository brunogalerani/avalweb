def professor():    
	if(session.user_prof):
		redirect(URL('controlesprofessor', 'home'))
	else:
		labels = {'user_prof':'Usuário', 'passw_prof':'Senha'}
		form = SQLFORM.factory(
        Field('user_prof', requires=IS_NOT_EMPTY()),
        Field('passw_prof', 'password', requires=IS_NOT_EMPTY()),
        labels = labels,
        submit_button='Login')

	if form.process().accepted:
		for row in db().select(db.professor.id, db.professor.user_prof, db.professor.passw_prof):
			if row.user_prof == form.vars.user_prof and row.passw_prof == form.vars.passw_prof:
				session.user_prof = row.id
				redirect(URL('controlesprofessor', 'home'))
		 			
		response.flash=T("Usuário ou senha errados!")		
	return dict(form=form)

def aluno():    
	if(session.user_aluno):
		redirect(URL('controlesaluno', 'home'))
	else:
		labels = {'user_aluno':'Usuário', 'passw_aluno':'Senha'}
		form = SQLFORM.factory(
        Field('user_aluno', requires=IS_NOT_EMPTY()),
        Field('passw_aluno', 'password', requires=IS_NOT_EMPTY()),
        labels = labels,
        submit_button='Login')

	if form.process().accepted:
		for row in db().select(db.aluno.user_aluno, db.aluno.passw_aluno):
			if row.user_aluno == form.vars.user_aluno and row.passw_aluno == form.vars.passw_aluno:
				session.user_aluno = row.user_aluno
				redirect(URL('controlesaluno', 'home'))
		 			
		response.flash=T("Usuário ou senha errados!")		
	return dict(form=form)	
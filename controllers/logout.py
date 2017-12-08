def logout():
	if session.user_prof:
		session.user_prof = None
	elif session.user_aluno:
		session.user_aluno = None
	
	redirect(URL('default', 'index'))
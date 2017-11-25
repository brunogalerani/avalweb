def logout():
	if session.user_prof:
		session.user_prof = None
		redirect(URL('login', 'professor'))
	elif session.user_aluno:
		session.user_aluno = None
		redirect(URL('login', 'aluno'))
	else:
		redirect(URL('default', 'index'))
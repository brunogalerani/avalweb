def index():        
	if(session.user_prof):
		redirect(URL('controlesprofessor', 'home'))
	if(session.user_aluno):	
		redirect(URL('controlesaluno', 'home'))

	return dict()
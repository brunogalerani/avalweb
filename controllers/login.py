def professor():    
	if(session.user):
		redirect('http://www.yahoo.com.br')
	return dict()
	
def log():
	for row in db().select(db.professor.user_prof):
		if row.user_prof == request.vars['user_prof']:
			session.user = row.user_prof
			redirect('http://www.web2py.com')
	
	redirect('http://www.google.com')
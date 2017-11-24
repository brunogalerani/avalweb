def aluno():
    form = SQLFORM(db.aluno)    
    if form.accepts(request.vars, session):
        response.flash = 'Cadastrado com sucesso'        
    return dict(form=form)
    
def professor():
    form = SQLFORM(db.professor)    
    if form.accepts(request.vars, session):
        response.flash = 'Cadastrado com sucesso'        
    return dict(form=form)
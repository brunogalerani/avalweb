def index():
    
    form = SQLFORM(db.aluno_dados)    
    if form.accepts(request.vars, session):
        response.flash = 'deu bom'
        
    return dict(form=form)

def home():
    return dict(usuario=request.vars.login)

def user():
    return dict()

def dados():
    list = []
    for elem in db(db.aluno_dados).select():
        list.append(elem.name + "<br>")
    return list
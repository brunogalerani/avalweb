def index():
    
    form = SQLFORM(db.teste)
    def validate(form):
        if form.vars.name != '' :
            db.teste.insert(name=form.vars.name)
        else:
            form.errors.name = 'insira dados'
    
    if form.accepts(request.vars, session, onvalidation = validate):
        response.flash = 'deu bom'
        
    return dict(form=form)

def home():
    return dict(usuario=request.vars.login)

def user():
    return dict()

def dados():
    list = []
    for elem in db(db.teste).select():
        list.append(elem.name + "<br>")
    return list
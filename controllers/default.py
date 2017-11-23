import os 

def index():    
    form = SQLFORM(db.questoes)    
    if form.accepts(request.vars, session):
        response.flash = 'deu bom'
        
    return dict(form=form)

def home():
    list = []
    company_rec = db(db.questoes).select().first()
    video = os.path.join(request.folder, 'uploads', company_rec.video_enunc)
    return dict(video_enunc = video)

def show_logo():
    return response.download(request, db)

def user():
    return dict()

def dados():
    list = []
    for elem in db(db.professor).select():
        list.append(elem.name + "<br>")
    return list


def cadastro():
    form = SQLFORM(db.professor)
    if form.accepts(request.vars, session):
        response.flash = 'deu bom'

    return dict(form=form)

def login():
    form = SQLFORM(db.professor)
    if form.accepts(request.vars, session):
        response.flash = 'deu bom'

    return dict(form=form)
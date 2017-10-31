def index():
    return dict(message='Hello World')

def home():
    return dict(usuario=request.vars.login)
db=DAL('mysql://root:root@localhost/avalweb');

db.define_table(
    'aluno',
    Field('user_aluno', length=64, requires=IS_NOT_EMPTY(), unique=True),
    Field('passw_aluno', 'password', requires=IS_NOT_EMPTY()),
    Field('nome_aluno', requires=IS_NOT_EMPTY()),
    Field('email_aluno', length=100, requires=IS_NOT_EMPTY(), unique=True),
);

db.define_table(
    'professor',
    Field('user_prof', length=64, requires=IS_NOT_EMPTY(), unique=True),
    Field('passw_prof', 'password', requires=IS_NOT_EMPTY()),
    Field('nome_prof', requires=IS_NOT_EMPTY()),
    Field('email_prof', length=100, requires=IS_NOT_EMPTY(), unique=True),
);

db.define_table(
    'questoes',
    Field('topic_name', requires=IS_NOT_EMPTY()),
    Field('user_prof', db.professor, requires=IS_NOT_EMPTY(), writable=False),
    Field('enunciado', 'text', requires=IS_NOT_EMPTY()),
    Field('video_enunc', 'upload', default='', requires=IS_NOT_EMPTY()),
    Field('resposta', 'text', requires=IS_NOT_EMPTY()),
    Field('resp1', 'text', requires=IS_NOT_EMPTY()),
    Field('resp2', 'text', requires=IS_NOT_EMPTY()),
    Field('resp3', 'text', requires=IS_NOT_EMPTY()),
    Field('feed_resp', 'text', requires=IS_NOT_EMPTY()),
    Field('feed_r1', 'text', requires=IS_NOT_EMPTY()),
    Field('feed_r2', 'text', requires=IS_NOT_EMPTY()),
    Field('feed_r3', requires=IS_NOT_EMPTY()),    
    Field('dificuldade', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Fácil', 'Médio', 'Difícil'])]),
    Field('acerto_goto', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Fácil', 'Médio', 'Difícil'])]),
    Field('erro_goto', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Fácil', 'Médio', 'Difícil'])]),
    Field('topic', 'text', requires=IS_NOT_EMPTY()),
    Field('parte', 'text', requires=IS_NOT_EMPTY())
)

db.define_table(
    'provas',    
    Field('user_prof', db.professor, writable=False),
    Field('topic_name', requires=IS_NOT_EMPTY()),
    Field('modo_prova', requires=IS_NOT_EMPTY()),
    Field('aval', requires=IS_NOT_EMPTY())
)

db.define_table(
    'provasd',
    Field('cod_prova', db.provas, requires=IS_NOT_EMPTY()),
    Field('user_prof', db.professor, writable=False),
    Field('tempo', 'time', requires=IS_NOT_EMPTY()),
    Field('dificuldade', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Fácil', 'Médio', 'Difícil'])]),
    Field('dif_inicio', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Fácil', 'Médio', 'Difícil'])]),
    Field('topic_name', requires=IS_NOT_EMPTY()),
    Field('parte', requires=IS_NOT_EMPTY()),
    Field('num_total', 'integer', requires=IS_NOT_EMPTY()),
)

db.define_table(
    'provase',
    Field('cod_prova', db.provas, requires=IS_NOT_EMPTY()),
    Field('user_prof', db.professor, writable=False),
    Field('tempo', 'time', requires=IS_NOT_EMPTY()),
    Field('num_e', 'integer', requires=IS_NOT_EMPTY()),
    Field('num_m', 'integer', requires=IS_NOT_EMPTY()),
    Field('num_h', 'integer', requires=IS_NOT_EMPTY()),
    Field('topic_name', requires=IS_NOT_EMPTY()),
    Field('parte', requires=IS_NOT_EMPTY()),
    Field('num_total', 'integer', requires=IS_NOT_EMPTY()),
    Field('cod_questoes', requires=IS_NOT_EMPTY()),
)

db.define_table(
    'provas_uploads',
    Field('user_prof', db.professor, writable=False),
    Field('user_aluno', db.aluno, writable=False),
    Field('cod_prova', db.provas, writable=False),
    Field('nota', 'double', writable=False),
    Field('prova_up', 'upload', default='')
)

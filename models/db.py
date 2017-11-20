db=DAL('mysql://root:root@localhost/avalweb');

db.define_table(
    'aluno_login',
    Field('user_aluno', length=64),
    Field('passw_aluno'),
    primarykey=['user_aluno']
);

db.define_table(
    'login',
    Field('user', length=64),
    Field('passw'),
    primarykey=['user']
);

db.define_table(
    'aluno_dados',
    Field('user_aluno', db.aluno_login),
    Field('nome_aluno'),
    Field('email_aluno'),
    primarykey=['user_aluno']
);

db.define_table(
    'professor',
    Field('user_prof', db.login),
    Field('nome_prof'),
    Field('email_prof'),
    primarykey=['user_prof']
);

db.define_table(
    'questoes',    
    Field('topic_name'),
    Field('user_prof', db.login),
    Field('enunciado', 'text'),
    Field('video_enunc', 'upload', default=''),
    Field('resposta', 'text'),
    Field('resp1', 'text'),
    Field('resp2', 'text'),
    Field('resp3', 'text'),
    Field('feed_resp', 'text'),
    Field('feed_r1', 'text'),
    Field('feed_r2', 'text'),
    Field('feed_r3', 'text'),
    Field('video_resp', 'upload', default=''),
    Field('video_r1', 'upload', default=''),
    Field('video_r2', 'upload', default=''),
    Field('video_r3', 'upload', default=''),
    Field('dificuldade', 'text'),
    Field('acerto_goto', 'text'),
    Field('erro_goto', 'text'),
    Field('topic', 'text'),
    Field('parte', 'text')
)

db.define_table(
    'provas',
    Field('cod_prova', 'integer'),
    Field('user_prof', db.login),
    Field('topic_name'),
    Field('modo_prova'),
    Field('aval')
)

db.define_table(
    'provasd',
    Field('cod_prova', db.provas),
    Field('user_prof', db.login),
    Field('tempo', 'time'),
    Field('dificuldade'),
    Field('dif_inicio'),
    Field('topic_name'),
    Field('parte'),
    Field('num_total', 'integer'),
    primarykey=['cod_prova']
)

db.define_table(
    'provase',
    Field('cod_prova', db.provas),
    Field('user_prof', db.login),
    Field('tempo', 'time'),
    Field('num_e', 'integer'),
    Field('num_m', 'integer'),
    Field('num_h', 'integer'),
    Field('topic_name'),
    Field('parte'),
    Field('num_total', 'integer'),
    Field('cod_questoes'),
    primarykey=['cod_prova']
)

db.define_table(
    'provas_uploads',
    Field('user_prof', db.login),
    Field('user_aluno', db.aluno_login),
    Field('cod_prova', db.provas),
    Field('nota', 'double'),
    Field('prova_up', 'upload', default='')
)
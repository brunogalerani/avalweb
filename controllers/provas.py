def provas_dinamica():

	return dict()

def provas_estatica():
	provaId = session.estatica
	row = db(db.provase.id==provaId, db.provase.cod_questoes).select().first()

	questoes = row.cod_questoes.split(',')
	fields = []
	labels = {}
	imagens = []

	for i in range(len(questoes)):
		dicionario = {}
		questao = db(db.questoes.id==int(questoes[i]), db.questoes.ALL).select().first()
		labels.update({"questao" + str(i+1):questao.enunciado})
		dicionario.update({"certo":questao.resposta, "errado1":questao.resp1, "errado2":questao.resp2, "errado3":questao.resp3})
		field = Field('questao' + str(i+1), requires=IS_IN_SET(dicionario), widget=SQLFORM.widgets.radio.widget)
		fields.append(field)
		imagens.append(questao.video_enunc)

	form = SQLFORM.factory(*fields, labels=labels)
	return dict(form=form, imagens=imagens)
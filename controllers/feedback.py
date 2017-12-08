def feed_provas():
	professorId = session.user_prof
	info_provas = db(db.provas_uploads.user_prof == professorId, db.provas_uploads.ALL).select()

	html = "<table><thead><tr><th>Qtd. Provas</th><th>Média Geral</th><th>Qtd. Acertos</th><th>Qtd. Erros</th></tr></thead>"

	quantidade = len(info_provas)
	notas = 0
	acertos = 0	
	erros = 0

	if len(info_provas) == 0:
		return {"feeds" : XML(html)}

	for row in info_provas:
		notas += row.nota	

	media = notas/quantidade

	html += "<tbody><tr><td>" + str(quantidade) + "</td><td>" + str(media) + "</td><td>" + str(acertos) + "</td>"
	html += "<td>" + str(erros) + "</td></tr></tbody>"
	html += "</table>"
	return {"feeds" : XML(html)}
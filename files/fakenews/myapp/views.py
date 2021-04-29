from django.shortcuts import render
from django.http import HttpResponse

def evaluate_url(url):
	from . import scraper
	article_data = scraper.scrape(url)
	import joblib
	import os
	root_path = os.path.join('..', '..')
	path = os.path.join(root_path, 'model.joblib') 
	model = joblib.load(path)
	res = model.predict([article_data['text']])
	if res == 1:
		return "TRUE"
	else:
		return "FAKE"

def index(request):
	if request.method == 'POST':
		url = request.POST['link'][0]
		result = evaluate_url(url)
	else: result = None
	return render(request, 'index.html', {'result': result})

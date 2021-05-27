from django.shortcuts import render
from django.http import HttpResponse

import joblib
import os
from . import scraper


root_path = os.path.join('..', '..')
path = os.path.join(root_path, 'model.joblib') 
model = joblib.load(path)

def evaluate_url(url):
	article_data = scraper.scrape(url)
	print(url, article_data)
	if article_data == {}:
		return "UNABLE TO COLLECT ARTICLE"

	res = model.predict([article_data['text']])
	if res == 1:
		return "TRUE"
	else:
		return "FAKE"

def index(request):
	if request.method == 'POST':
		print(request.POST['link'])
		url = request.POST['link']
		result = evaluate_url(url)
	else: 
		result = None
		url = ""
	return render(request, 'index.html', {'result': result, 'given_url': url})

def about(request):
	return render(request, 'about.html')
	
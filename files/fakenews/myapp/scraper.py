from newspaper import Article
import datetime
import pytz
def scrape(url):
    article = Article(url, request_timeout = 5)
    try:
        article.download()
        article.parse()
        print("Building", article.title)
    except Exception as e:
        print(str(e))
        return {}

    if not article.text: return {}
    
    doc = {}
    doc['title'] = article.title
    doc['date'] = datetime.datetime.now(pytz.utc).isoformat()
    doc['url'] = article.url
    doc['text'] = article.text 
    # doc['html'] = article.article_html
    return doc

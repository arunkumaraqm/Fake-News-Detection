from newspaper import Article
import datetime
import pytz
def scrape(url):
    article = Article(url, request_timeout = 5)
    try:
        article.download()
        article.parse()
        print("Building", article.title)
    except:
        print("Couldn't download article")

    doc = {}
    doc['title'] = article.title
    doc['date'] = datetime.datetime.now(pytz.utc).isoformat()
    doc['url'] = article.url
    doc['content'] = article.text 
    # doc['html'] = article.article_html
    return doc

print(scrape(r'https://www.msn.com/en-us/news/us/dc-officer-who-suffered-heart-attack-on-jan-6-calls-out-trump-for-downplaying-e2-80-98brutal-savage-e2-80-99-riot/ar-BB1g84LI'))
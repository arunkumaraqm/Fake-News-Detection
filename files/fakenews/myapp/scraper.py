from newspaper import Article
import datetime
import pytz

# def scrape(url):
#     article = Article(url, request_timeout = 5)
#     try:
#         article.download()
#         article.parse()
#         print("Building", article.title)
#     except:
#         print("Couldn't download article")

#     doc = {}
#     doc['title'] = article.title
#     doc['date'] = datetime.datetime.now(pytz.utc).isoformat()
#     doc['url'] = article.url
#     doc['text'] = article.text 
#     # doc['html'] = article.article_html
#     return doc

def scrape(url):
    import os

    root_path = os.path.join('..', '..')
    path = os.path.join(root_path, 'data-umich', 'fakeNewsDataset', 'legit', 'polit40.legit.txt')
    title, text = "", ""
    with open(path, 'r') as fin:
        title = fin.readline()
        text = fin.read()
        print(title, text)
    return {'title': title, 'text': text}

if __name__ == '__main__':
    print(scrape(r'https://www.msn.com/en-us/news/us/dc-officer-who-suffered-heart-attack-on-jan-6-calls-out-trump-for-downplaying-e2-80-98brutal-savage-e2-80-99-riot/ar-BB1g84LI'))
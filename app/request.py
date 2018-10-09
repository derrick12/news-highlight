import urllib.request,json
from .models import Source,Article
import ssl

# Getting api key 
api_key = None

# Getting the source url
news_sources_url = None

# Getting the articles url
articles_url = None

# Articles class to define Articles Objects
Article = Article

# Source class to define Source Objects
Source = Source

# Create a SSLContext object with default settings.
ssl._create_default_https_context = ssl._create_unverified_context


def configure_request(app):
    '''
    Function that takes in the application instance and replaces
    the values of the None variables to application configurationn objects
    '''

    global api_key,news_sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]
    articles_url = app.config["SPECIFIC_SOURCE_API_URL"]



def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?language=en&q={}&apiKey={}'.format(article_name,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_articles_results(search_article_list)

    return search_article_results


def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(source_id,api_key)

    # We use 'with' as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list) # function that takes in the list of dictionary objects and returns a list of movie objects

    return articles_results


def get_sources(category):
    '''
    Function that gets the json response to url request 
    '''
    get_sources_url = news_sources_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

    return source_results



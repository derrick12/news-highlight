from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles,search_article


# Views 
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting sources
    general_sources = get_sources('general')
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    entertainment_sources = get_sources('entertainment')

    title = 'Home - Welcome to The Best News Website Online'
    search_article = request.args.get('article_query')

    # if the search value actually exists if it does we use the 'redirect' function that redirects us to another view function
    if search_article:
        return redirect(url_for('main.search',article_name = search_article))
    else:
        return render_template('index.html', title = title, general = general_sources, technology = technology_sources, business = business_sources, sports = sports_sources, health = health_sources, science = science_sources, entertainment = entertainment_sources)


@main.route('/articles/<source>')
def articles(source):
    '''
    View function to diplay articles
    '''
    articles = get_articles(source)
    return render_template('article.html', articles = articles)


@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'

    return render_template('search.html',articles = searched_articles)
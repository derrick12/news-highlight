import os  # the os module will allow our application to interact with the operating system dependent functionality
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SPECIFIC_SOURCE_API_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class 
    
    Args:
        Config: The parent configuration class with General configuration setting
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with genneral configuartion settings
    '''
    DEBUG = True
# a dictionary config_options to help us access different configuration option classes
config_options = {
'development':DevConfig,
'production':ProdConfig
}

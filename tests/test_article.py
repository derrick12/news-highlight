import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article('Test author','Test title','Test description','Test url','Test image','Test publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

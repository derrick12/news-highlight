import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method to run before every test
        '''
        self.new_source = Source('Test id','Test name','Test description','Test categoty','Test language')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


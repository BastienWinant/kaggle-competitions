from commonlitDataset import Dataset
import unittest

class DatasetTestCase(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()
        
    def test_datatype(self):
        # self.assertEqual(type(self.dataset), "<class 'commonlitDataset.Dataset'>")
        self.assertIsInstance(self.dataset, Dataset)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DatasetTestCase('test_datatype'))
    return suite
    
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
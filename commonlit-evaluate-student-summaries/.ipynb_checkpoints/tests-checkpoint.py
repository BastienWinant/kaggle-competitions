from commonlitDataset import Dataset
import unittest
import os
import pandas as pd

class DatasetImportTestCase(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()
        
    def test_datatype(self):
        self.assertIsInstance(self.dataset, Dataset)
    
    def test_filepath_attributes(self):
        self.assertIsInstance(self.dataset.train_prompts_file, str)
        self.assertIsInstance(self.dataset.test_prompts_file, str)
        self.assertIsInstance(self.dataset.train_summaries_file, str)
        self.assertIsInstance(self.dataset.test_summaries_file, str)
    
    def test_filepath_existence(self):
        self.assertEquals(os.path.exists(self.dataset.train_prompts_file), True)
        self.assertEquals(os.path.exists(self.dataset.test_prompts_file), True)
        self.assertEquals(os.path.exists(self.dataset.train_summaries_file), True)
        self.assertEquals(os.path.exists(self.dataset.test_summaries_file), True)

    def test_train_data_read(self):
        self.dataset.load_training_data()
        self.assertIsInstance(self.dataset.train_prompts, pd.DataFrame)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DatasetImportTestCase('test_datatype'))
    suite.addTest(DatasetImportTestCase('test_filepath_attributes'))
    suite.addTest(DatasetImportTestCase('test_filepath_existence'))
    suite.addTest(DatasetImportTestCase('test_train_data_read'))
    return suite
    
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
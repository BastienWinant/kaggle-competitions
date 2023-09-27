from commonlitDataset import Dataset
import unittest
import os
import pandas as pd

# check the existence of data files
# and reads into pandas dataframes
class DatasetImportTestCase(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()

    # test Dataset class instantiation
    def test_datatype(self):
        self.assertIsInstance(self.dataset, Dataset)

    # test filepath attributes' datatypes
    def test_filepath_attributes(self):
        self.assertIsInstance(self.dataset.train_prompts_file, str)
        self.assertIsInstance(self.dataset.test_prompts_file, str)
        self.assertIsInstance(self.dataset.train_summaries_file, str)
        self.assertIsInstance(self.dataset.test_summaries_file, str)

    # test datafiles existence
    def test_filepath_existence(self):
        self.assertEquals(os.path.exists(self.dataset.train_prompts_file), True)
        self.assertEquals(os.path.exists(self.dataset.test_prompts_file), True)
        self.assertEquals(os.path.exists(self.dataset.train_summaries_file), True)
        self.assertEquals(os.path.exists(self.dataset.test_summaries_file), True)

    # test train data read into dataframes
    def test_train_data_read(self):
        self.dataset.load_data()
        self.assertIsInstance(self.dataset.train_prompts, pd.DataFrame)
        self.assertIsInstance(self.dataset.train_summaries, pd.DataFrame)

    # test test data read into dataframes
    def test_test_data_read(self):
        self.dataset.load_data(training=False)
        self.assertIsInstance(self.dataset.test_prompts, pd.DataFrame)
        self.assertIsInstance(self.dataset.test_summaries, pd.DataFrame)

def DatasetCleaningTestCase(unittest.TestCase):
    def setUp():
        self.dataset = Dataset()
        
    def test_merge_columns():
        pass
        
def DataImportTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(DatasetImportTestCase('test_datatype'))
    suite.addTest(DatasetImportTestCase('test_filepath_attributes'))
    suite.addTest(DatasetImportTestCase('test_filepath_existence'))
    suite.addTest(DatasetImportTestCase('test_train_data_read'))
    return suite

def DataCleanTestSuite():
    suite = unittest.TestSuite()
    return suite
    
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(DataImportTestSuite())
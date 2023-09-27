from commonlitDataset import Dataset
import unittest
import os
import pandas as pd

# test the existence of data files and reads into pandas dataframes
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
        self.assertEqual(os.path.exists(self.dataset.train_prompts_file), True)
        self.assertEqual(os.path.exists(self.dataset.test_prompts_file), True)
        self.assertEqual(os.path.exists(self.dataset.train_summaries_file), True)
        self.assertEqual(os.path.exists(self.dataset.test_summaries_file), True)

    # test train data read into dataframes
    def test_train_data_read(self):
        prompts_df, summaries_df = self.dataset.load_data()
        
        self.assertIsInstance(prompts_df, pd.DataFrame)
        self.assertIsInstance(summaries_df, pd.DataFrame)

    # test test data read into dataframes
    def test_test_data_read(self):
        prompts_df, summaries_df = self.dataset.load_data(training=False)
        
        self.assertIsInstance(prompts_df, pd.DataFrame)
        self.assertIsInstance(summaries_df, pd.DataFrame)

# test the validity of the import data files
class DatasetCleanTestCase(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()
        
    def test_train_merge_columns(self):
        prompts_df, summaries_df = self.dataset.load_data()

        prompts_df_columns = prompts_df.columns
        summaries_df_columns = summaries_df.columns
        merge_candidates = prompts_df_columns.intersection(summaries_df_columns)

        # verify that at least one column is shared between the dataframes
        self.assertGreater(len(merge_candidates), 0)

        # verify that no null values are in the merging candidates
        for column in merge_candidates:
            self.assertEqual(prompts_df[column].isna().sum(), 0)
            self.assertEqual(summaries_df[column].isna().sum(), 0)

    def test_test_merge_columns(self):
        prompts_df, summaries_df = self.dataset.load_data(training=False)

        prompts_df_columns = prompts_df.columns
        summaries_df_columns = summaries_df.columns
        merge_candidates = prompts_df_columns.intersection(summaries_df_columns)

        # verify that at least one column is shared between the dataframes
        self.assertGreater(len(merge_candidates), 0)
        
        # verify that no null values are in the merging candidates
        for column in merge_candidates:
            self.assertEqual(prompts_df[column].isna().sum(), 0)
            self.assertEqual(summaries_df[column].isna().sum(), 0)
        
        
def DatasetImportTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(DatasetImportTestCase('test_datatype'))
    suite.addTest(DatasetImportTestCase('test_filepath_attributes'))
    suite.addTest(DatasetImportTestCase('test_filepath_existence'))
    suite.addTest(DatasetImportTestCase('test_train_data_read'))
    return suite


def DatasetCleanTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(DatasetCleanTestCase('test_train_merge_columns'))
    suite.addTest(DatasetCleanTestCase('test_test_merge_columns'))
    return suite
    
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(DatasetImportTestSuite())
    runner.run(DatasetCleanTestSuite())
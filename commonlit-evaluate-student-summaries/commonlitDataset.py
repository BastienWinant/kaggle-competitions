import numpy as np
import pandas as pd

class Dataset:
    def __init__(self):
        self.train_prompts_file = "./data/prompts_train.csv"
        self.test_prompts_file = "./data/prompts_test.csv"

        self.train_summaries_file = "./data/summaries_train.csv"
        self.test_summaries_file = "./data/summaries_test.csv"

    def load_data(self, training=True):
        prompts_df = None
        summaries_df = None
        
        if training:
            prompts_df = pd.read_csv(self.train_prompts_file)
            summaries_df = pd.read_csv(self.train_summaries_file)
        else:
            prompts_df = pd.read_csv(self.test_prompts_file)
            summaries_df = pd.read_csv(self.test_summaries_file)

        return prompts_df, summaries_df
        
    # def merge_data(self, training=True):
    #     prompt_da

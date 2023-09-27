import numpy as np
import pandas as pd

class Dataset:
    def __init__(self):
        self.train_prompts_file = "./data/prompts_train.csv"
        self.test_prompts_file = "./data/prompts_test.csv"

        self.train_summaries_file = "./data/summaries_train.csv"
        self.test_summaries_file = "./data/summaries_test.csv"

    def load_data(self, training=True):
        if training:
            self.train_prompts = pd.read_csv(self.train_prompts_file)
            self.train_summaries = pd.read_csv(self.train_summaries_file)
        else:
            self.test_prompts = pd.read_csv(self.test_prompts_file)
            self.test_summaries = pd.read_csv(self.test_summaries_file)
        # self.train_prompts = pd.read_csv(train_prompts_file)
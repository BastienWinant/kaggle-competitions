import numpy as np
import pandas as pd

class Dataset:
    def __init__(self):
        self.train_prompts_file = "./data/prompts_train.csv"
        self.test_prompts_file = "./data/prompts_test.csv"

        self.train_summaries_file = "./data/summaries_train.csv"
        self.test_summaries_file = "./data/summaries_test.csv"

    def load_training_data(self):
        self.train_prompts = None
        # self.train_prompts = pd.read_csv(train_prompts_file)
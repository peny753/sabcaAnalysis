import pandas as pd
import csv



def load_data_reference(filename):
	reference = pd.read_csv(filename, delimiter=';')
	return reference


def load_table(filename):
	data = pd.read_csv(filename, delimiter='\t', low_memory=False, index_col=0)
	return data

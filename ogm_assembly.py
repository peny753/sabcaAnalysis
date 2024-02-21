import pandas as pd
import csv


def load_data_reference(filename):
	reference = pd.read_csv(filename, delimiter=';')
	return reference


def load_table(filename):
	data = pd.read_csv(filename, delimiter='\t', low_memory=False, index_col=0)
	return data


def check_filter_value(row):
	return int(row['FILTER'].split(';')[1].split('=')[1]) >= 3


def compare_min_max_values(position, min_val, max_val, min_range, max_range):
	return min_range <= abs(position - min_val) <= max_range or min_range <= abs(position - max_val) <= max_range


# TODO: correct comumns
# TODO: chcek chromosome 23
def resolve_row(chromosome_type, data_row, reference_row, min_range, max_range):
	if str(data_row[chromosome_type]) == str(reference_row['Chr_from']) and reference_row['Type'] != 'translocation':
		if (compare_min_max_values(int(data_row['PosFrom']), int(reference_row['RefStartPos']), int(reference_row['RefEndPos']), min_range, max_range)) or \
				(compare_min_max_values(int(data_row['PosTo']), int(reference_row['RefStartPos']), int(reference_row['RefEndPos']), min_range, max_range)):
			return True

	return False


def compare_with_reference(data_row, reference, min_range, max_range):
	for index, reference_row in reference.iterrows():
		if resolve_row('ChrFrom', data_row, reference_row, min_range, max_range) or \
				resolve_row('ChrTo', data_row, reference_row, min_range, max_range):
			return True

	return False


def is_row_valid(row, reference, min_range, max_range):
	if check_filter_value(row):
		if compare_with_reference(row, reference, min_range, max_range):
			return True

	return False


def write_line_to_file(row, file_path):
	with open(file_path, 'a', newline='', encoding='utf-8') as result_file:
		writer = csv.writer(result_file, delimiter='\t')
		writer.writerow(row)


def process_data(reference_filepath, data_filepath, result_path, min_range, max_range):
	reference = load_data_reference(reference_filepath)
	data = load_table(data_filepath)
	counter = 0

	for index, row in data.iterrows():

		if row['ChrFrom'] == './.:.:.,.':
			continue

		if is_row_valid(row, reference, min_range, max_range):
			write_line_to_file(row, result_path)
			print(index, row)
			counter += 1

	print(counter)

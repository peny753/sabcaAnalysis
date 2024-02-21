import chip_cytoscan_analysis as chip
import ogm_assembly as assembly
import ogm_rare as rare


if __name__ == '__main__':
	# chip.process_data('table_folder/4/BRNO1440_3261.csv', 'table_folder/4/Dedup_1000distDistanced_BRNO1440.tsv', 'table_folder/4/result.tsv', 0, 10000)
	# assembly.process_data('table_folder/1/OGM Assambly.csv', 'table_folder/1/Dedup_1000distDistanced_BRNO2641_copy.tsv', 'table_folder/1/result_assembly.tsv', 0, 10000)
	rare.process_data('table_folder/1/OGM Rare Analysis.csv', 'table_folder/1/Dedup_1000distDistanced_BRNO2641_copy.tsv', 'table_folder/1/result_rare.tsv', 10000, 20000)


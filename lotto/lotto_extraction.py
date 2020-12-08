from lotto.lotto_numbers import NumbersForExtraction
from lotto.lotto_tables import print_extraction


class Extraction:
    """
    represents an extraction table, namely one extraction for each "ruota" (10 extractions in total)
    @attr all_extractions is a dictionary with cities as keys and list of extracted numbers as values
    """
    all_cities = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self):
        self.all_extractions = {}
        for city in Extraction.all_cities:
            # to check
            self.all_extractions[city] = NumbersForExtraction().sequence

    def __str__(self):
        extraction_dictionary = self.all_extractions
        print_extraction(extraction_dictionary)
        return ''


if __name__ == '__main__':
    extraction_test = Extraction()
    print(extraction_test.all_extractions)  # valid
    print()
    print(extraction_test)

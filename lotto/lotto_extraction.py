from lotto.lotto_city import City
from lotto.lotto_numbers import NumbersForExtraction
from lotto.lotto_tables import print_extraction

class Extraction:
    all_cities = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self):
        self.extraction = {}
        for city in Extraction.all_cities:
            # to check
            self.extraction[city] = NumbersForExtraction().numbers


    def __str__(self):
        extraction_dictionary = self.extraction
        print_extraction(extraction_dictionary)
        return ''


if __name__ == '__main__':
    extraction_test = Extraction()
    print(extraction_test.extraction) # valid
    print()
    print(extraction_test)


        
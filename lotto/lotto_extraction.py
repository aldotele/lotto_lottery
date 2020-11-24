from lotto.lotto_city import City
from lotto.lotto_numbers import NumbersForExtraction

class Extraction:
    all_cities = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self):
        self.extraction = {}
        for city in Extraction.all_cities:
            # to check
            self.extraction[city] = NumbersForExtraction().numbers


    def print_extraction(self):
        print('+' + '-'*33 + '+')
        for city in self.extraction:
            int_sequence = self.extraction[city]
            str_sequence = [str(el) for el in int_sequence]
            sequence = '  '.join(str_sequence)
            print('|%10s' % city, end = '  ')
            for number in int_sequence:
                print('%.2d' % number, end='  ')
            print(' |')
        print('+' + '-'*33 + '+')


    def __str__(self):
        self.print_extraction()
        return ''


if __name__ == '__main__':
    extraction_test = Extraction()
    print(extraction_test.extraction) # valid
    print()
    print(extraction_test)


        
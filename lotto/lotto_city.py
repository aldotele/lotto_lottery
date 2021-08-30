class City:
    """
    represents the city aka "ruota" of extraction
    @attr name is the name of the city as a capitalized string
    @attr id is a numeric value which the city is associated to
    """
    city_strings = {1: 'Bari', 2: 'Cagliari', 3: 'Firenze', 4: 'Genova', 5: 'Milano', 6: 'Napoli', 7: 'Palermo',
                  8: 'Roma', 9: 'Torino', 10: 'Venezia', 11: 'Tutte'}

    city_codes = {'Bari': 1, 'Cagliari': 2, 'Firenze': 3, 'Genova': 4, 'Milano': 5, 'Napoli': 6, 'Palermo': 7,
                  'Roma': 8, 'Torino': 9, 'Venezia': 10, 'Tutte': 11}

    def __init__(self, city_code):
        if City.is_city_valid(city_code):
            city_code = int(city_code)
            self.name = City.city_strings[city_code]
            self.id = city_code
        else:
            raise ValueError('city code must be an integer between 1 and 11')

    @staticmethod
    def is_city_valid(city_code):
        try:
            city_code = int(city_code)
            if city_code in City.city_strings:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def show_city_list():
        for key in City.city_strings:
            print('{} : {}'.format(key, City.city_strings[key]))

    @staticmethod
    def get_cities():
        return list(City.city_strings.values())


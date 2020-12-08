class City:
    """
    represents the city aka the "ruota" of extraction
    @attr city_code is a numeric value which the city ("ruota") is associated to
    """
    all_cities = {1: 'Bari', 2: 'Cagliari', 3: 'Firenze', 4: 'Genova', 5: 'Milano', 6: 'Napoli', 7: 'Palermo',\
         8: 'Roma', 9: 'Torino', 10: 'Venezia', 11: 'Tutte'}

    def __init__(self, city_code):
        if City.is_city_valid(city_code):
            city_code = int(city_code)
            self.city = City.all_cities[city_code]
        else:
            return None
            

    @staticmethod
    def is_city_valid(city_code):
        try:
            city_code = int(city_code)
            if city_code in City.all_cities:
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def show_city_list():
        for key in City.all_cities:
            print('{} : {}'.format(key, City.all_cities[key]))


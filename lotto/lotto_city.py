
class City:
    """
    represents the city aka the "ruota" of extraction
    @attr city is one of the 10 allowed cities
    """
    all_cities = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self, city):
        # making sure that writing "ROMA", "roma" and "  rOmA   " is the same as writing "Roma" 
        city = city.strip().capitalize()
        if City.is_city_valid(city):
            self.city = city
        else:
            return None
            
    @staticmethod
    def is_city_valid(city):
        city = city.strip().capitalize()
        if city in City.all_cities:
            return True
        else:
            print('NOT VALID: city must be spelled correctly')
            return False


# tests
if __name__ == '__main__':
    mycity = City('Milano')
    print(City.is_city_valid('MIlano'))
    #print(mycity.city)

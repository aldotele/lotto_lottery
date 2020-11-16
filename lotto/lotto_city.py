
class City:
    # la seguente è una proprietà della classe e non dell'istanza
    all_cities = ['Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia']

    def __init__(self, city):
        # faccio in modo che "ROMA", "roma", "   roma", "  rOmA   " etc. corrispondano tutte a "Roma" 
        city = city.strip().capitalize()
        if self.is_city_valid(city):
            self.city = city
        else:
            raise ValueError('city not valid.\nPlease type one of the following cities ---> {}'.format(' '.join(City.all_cities)))

    def is_city_valid(self, city):
        if city in City.all_cities:
            return True
        else:
            return False

# tests
if __name__ == '__main__':
    mycity = City('milan')
    print(mycity.city)

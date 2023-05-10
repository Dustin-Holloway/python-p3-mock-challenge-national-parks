class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise Exception("Name must be a string and between 1 and 15 characters.")


    @property
    def name(self):
        return self._name




    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]
       
    
    def national_parks(self):
        from classes.trip import Trip
        return list(set([park.national_park for park in Trip.all if park.visitor == self]))


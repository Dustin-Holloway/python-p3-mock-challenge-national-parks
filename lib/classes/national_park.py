class NationalPark:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise Exception("Should be a string.")
        NationalPark.all.append(self)


    @property
    def name(self):
            return self._name

    

        
    def trips(self):
        from classes.trip import Trip
        return [tr for tr in Trip.all if tr.national_park == self]
 
    def visitors(self):
        from classes.trip import Trip
        return list(set([vis.visitor for vis in Trip.all if vis.national_park == self]))

    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        from classes.trip import Trip   
        parks_list = [vis.visitor for vis in Trip.all if vis.national_park == self]
        return max(parks_list, key = parks_list.count)


        
        



        
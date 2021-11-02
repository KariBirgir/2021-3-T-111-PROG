from animal import Animal
from island import Island

class Prey(Animal):
    MAX_OFFSPRING = 2    
    
    def __init__(self, island, x=0, y=0, name='O'):
        super().__init__(island, x, y, name)        #or Animal.__init__(self, island, x, y, name)

    def breed(self):
        '''Breed a new Animal.  If there is room in one of the neigboring locations,
        place the new animal there.'''
        if self._breed_clock <= 0:
            location = self._check_grid_for_neighbor(type(Island.UNOCCUPIED))
            if location != Animal.NOT_FOUND:
                the_class = self.__class__
                if MAX_OFFSPRING == 1:
                    # Reset the breed clock
                    self._breed_clock = the_class.breed_time    # breed_time is a class variable
                else: 
                    # Create an instance of a new animal
                    new_animal = the_class(self._island, x=location[0], y=location[1])
                    self._island.register(new_animal)
                    location = self._check_grid_for_neighbor(type(Island.UNOCCUPIED))
                    if location != Animal.NOT_FOUND:
                        the_class = self.__class__
                        # Reset the breed clock
                        self._breed_clock = the_class.breed_time    # breed_time is a class variable
                        # Create an instance of a new animal
                        new_animal = the_class(self._island, x=location[0], y=location[1])
                        self._island.register(new_animal)
                    else:
                        self._breed_clock = the_class.breed_time

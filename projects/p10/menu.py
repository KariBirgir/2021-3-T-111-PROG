class Menu():
    def __init__(self):
        self.options = []


    def add(self, option):
        '''Adds the given option to the end of this menu'''
        self.options.append(option)


    def remove(self, option):
        '''Removes the given option from the menu'''
        self.options.remove(option)


    def insert(self, option, pos):
        '''Inserts the given option at position pos'''
        if pos >= 1:
            self.options.insert(pos-1, option)  # list insert() is 0 based


    def position(self, option):
        '''Returns the position of the given option, or 0 if not found'''
        for idx, my_option in enumerate(self.options):
            if my_option == option:
                return idx + 1
        
        return 0


    def __str__(self):
        '''Returns a string representation of this menu'''
        menu_str = ""
        for i in range(len(self.options)):
            menu_str += "{}. {}\n".format(i+1, self.options[i])
        
        return menu_str
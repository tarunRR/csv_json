""" file for cleaning data """
class Operations:
    """ class for cleaning operations on data """
    def __init__(self, data):
        """ Initialising class """
        self.data = data
    def remove_empty_rows(self):
        """
        Removes all the empty rows from uploaded data
        """
        return self.data.dropna(how='all')

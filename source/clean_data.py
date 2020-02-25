class Operations:

    def __init__(self, data):
        self.data = data
    def remove_empty_rows(self):
        """
        Removes all the empty rows from uploaded data
        """
        return self.data.dropna(how='all')

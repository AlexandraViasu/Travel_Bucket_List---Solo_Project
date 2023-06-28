class City:

    def __init__(self, name, country, id = None):
        self.name = name
        self.id = id
        self.country = country

    def __repr__(self):
        return self.name

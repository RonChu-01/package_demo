class Fruit(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __init__(self):
        super().__init__()
        self._name = ''


f = Fruit()
f.name = 'ron'
print(f.name)


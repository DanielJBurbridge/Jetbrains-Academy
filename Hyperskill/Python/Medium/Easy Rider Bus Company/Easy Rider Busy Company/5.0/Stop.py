class Stop:
    def __init__(self, _id):
        self._id = _id
        self.name = None

    def __hash__(self):
        return hash(self.get_id())

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_id(self):
        return self._id

    def add_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

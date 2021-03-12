class BusLine:
    def __init__(self, _id):
        self._id = _id
        self.route = set()
        self.starting_stop = None
        self.finishing_stop = None

    def __hash__(self):
        return hash(self.get_id())

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_stop(self, stop):
        self.route.add(stop)

    def set_starting_stop(self, stop):
        if self.starting_stop is None:
            self.starting_stop = stop
        else:
            print("Starting stop already exists")

    def set_finishing_stop(self, stop):
        if self.finishing_stop is None:
            self.finishing_stop = stop
        else:
            print("Finishing stop already exists")

    def starting_and_finishing_exists(self):
        return bool(self.starting_stop and self.finishing_stop)

    def get_id(self):
        return self._id

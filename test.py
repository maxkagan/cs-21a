# Consider
# the
# following


# class definition:


class FifoQueue(list):
    """ implement a first in first out queue """

    capacity = 20

    def enqueue(self, item):
        if len(self) < self.capacity:
            self.append(item)

    def dequeue(self):
        if self:
            result = self.pop(0)
        else:
            result = None
        return result

    @property
    def available_spots(self):
        return self.capacity - len(self)


# and the
# following
# statements:
cs21 = FifoQueue()

cs21.enqueue('Daniel')

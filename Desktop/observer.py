#!/usr/bin/env python3

class Aggregator():
    # Agregator provides connection between generators and recievers
    # Methods:
    # add_generator(), add_reciever()
    # tick() - called by generators to publish data
    def __init__(self):
        self._generator_list = []
        self._reciever_list = []
        self._payload = None

    def add_generator(self,g):
        self._generator_list.append(g)
        g.connect(self)

    def add_reciever(self,r):
        self._reciever_list.append(r)

    def tick(self,payload):
        for item in self._reciever_list:
            item.recieve(payload)

    def remove_generator():
        pass

    def remove_reciever():
        pass

    def is_generator():
        pass

    def is_reciever():
        pass

    def is_changed():
        pass

    def clear_changed():
        pass

    def count_generators():
        pass

    def count_recievers():
        pass

class Generator():
    # Generator publishes updates of an object
    # Methods:
    # update() - passes data to Aggregator
    # connect() - connects an Aggregator (called by Aggregator only)
    def __init__(self):
        self._agr = None

    def update(self,payload):
        if self._agr is not None:
            self._agr.tick(payload)

    def connect(self,agr):
        self._agr = agr


class Reciever():
    # Reciever calls on_recieve() action when it recieves object from Aggregator
    # Methods:
    # set_on_recieve() - sets a reciever action
    # recieve() - calls reciever action
    # connect() - connects an Aggregator (called by Aggregator only)
    def __init__(self):
       self._on_recieve = None

    def recieve(self,payload):
        if self._on_recieve is not None:
            self._on_recieve(payload)

    def set_on_recieve(self,on_recieve_action):
        self._on_recieve = on_recieve_action

    def set_filter():
        pass

    def connect(self,agr):
        self._agr = agr


def main():
    a = Aggregator()
    g1 = Generator()
    g2 = Generator()
    r1 = Reciever()
    r2 = Reciever()
    r1.set_on_recieve(lambda x: print("R1 says ", x))
    r2.set_on_recieve(lambda x: print("R2 says ", x))
    a.add_generator(g1)
    a.add_generator(g2)
    a.add_reciever(r1)
    a.add_reciever(r2)
    g1.update("123")
    g2.update("234")



if __name__ == "__main__":
    main ()

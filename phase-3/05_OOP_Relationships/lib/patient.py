from .appointment import *

class Patient:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def appointments(self):
        pass

    def doctors(self):
        pass


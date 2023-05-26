from .appointment import *


class Doctor:
    all = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all.append(self)

    def appointments(self):
        return [appt for appt in Appointment.all if appt.doctor == self]

    def patients(self):
        return {appointment.patient for appointment in self.appointments()}

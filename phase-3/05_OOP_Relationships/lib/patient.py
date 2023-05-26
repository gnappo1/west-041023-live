from .appointment import *
from datetime import datetime
class Patient:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def appointments(self):
        return [appt for appt in Appointment.all if appt.patient == self]

    def sorted_appointments(self):
        return sorted(self.appointments(), key=lambda appt: datetime.strptime(appt.date, '%m/%d/%y'))
    
    def doctors(self):
        return {appointment.doctor for appointment in self.appointments()}

    def past_appointments(self):
        return [
            appt
            for appt in self.appointments()
            if datetime.strptime(appt.date, '%m/%d/%y') < datetime.today()
        ]

    def future_appointments(self):
        return set(self.appointments()) - set(self.past_appointments())

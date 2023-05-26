import datetime
class Appointment:
    all = []

    def __init__(self, doctor, patient, reason_for_visit, date):
        self.doctor = doctor
        self.patient = patient
        self.reason_for_visit = reason_for_visit
        self.date = date
        type(self).all.append(self)
        
    @classmethod
    def sorted_appts(cls):
        return sorted(cls.all, key=lambda appt: datetime.strptime(appt.date, '%m/%d/%y'))

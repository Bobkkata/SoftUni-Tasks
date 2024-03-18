from project_90_100.person import Person
from project_90_100.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

    
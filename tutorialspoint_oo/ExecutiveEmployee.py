from tutorialspoint_oo.Employee import Employee

class ExecutiveEmployee(Employee):

    def __init__(self, name, salary, car):
        Employee.__init__(self, name, salary)
        self.car = car

    def display_car(self):
        return self.car

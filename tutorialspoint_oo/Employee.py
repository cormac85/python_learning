#!/usr/bin/python


class Employee:
    """Common base class for all employees"""
    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1

    @staticmethod
    def display_count():
        print("Total Employees: %d" % Employee.employeeCount)

    def display_employee(self):
        print("Name: %s Salary: %d" % (self.name, self.salary))

    def __del__(self):
        className =  self.__class__.__name__
        print("Class %s has been destroyed." % className)


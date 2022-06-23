from employee import *

employee = Employee("Michael", "Jackson", 2012)


def test_email():
    assert employee.email == f"{employee.first}.{employee.last}@email.com"


def test_fullname():
    assert employee.fullname == f"{employee.first} {employee.last}"


def test_apply_raise():
    pay = employee.pay
    employee.apply_raise()
    assert employee.pay == int(pay * employee.raise_amt)

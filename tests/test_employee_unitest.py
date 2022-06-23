import unittest
from unittest.mock import patch, Mock
from employee import Employee


class TestEmployeeUnittest(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Leonardo", "DaVinci", 1337)
        super().setUp()

    def test_email(self):
        self.assertEqual(self.employee.email, f"{self.employee.first}.{self.employee.last}@email.com")

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, f"{self.employee.first} {self.employee.last}")

    def test_apply_raise(self):
        pay = self.employee.pay
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, int(pay*self.employee.raise_amt))

    @patch("requests.get")
    def test_monthly_schedule(self, request):
        request.return_value = Mock(ok=True, text="simple text")
        self.assertEqual(self.employee.monthly_schedule("Apr"), "simple text")

        request.return_value = Mock(ok=False, text="simple text")
        self.assertEqual(self.employee.monthly_schedule("Jun"), "Bad Response!")

import unittest
from fund import FundRecord


class TestFundRecord(unittest.TestCase):
    def setUp(self) -> None:
        self.fund_record = FundRecord(100)

    def test_calculate_reference_amount_when_temperature_less_than_10(self):
        self.fund_record.calculate_reference_amount(9)
        self.assertEqual(self.fund_record.reference_amount, 100)

    def test_calculate_reference_amount_when_temperature_between_10_and_20(self):
        self.fund_record.calculate_reference_amount(11)
        self.assertEqual(self.fund_record.reference_amount, 80)

    def test_calculate_reference_amount_when_temperature_between_20_and_25(self):
        self.fund_record.calculate_reference_amount(23)
        self.assertEqual(self.fund_record.reference_amount, 60)

    def test_calculate_reference_amount_when_temperature_between_25_and_30(self):
        self.fund_record.calculate_reference_amount(26)
        self.assertEqual(self.fund_record.reference_amount, 50)

    def test_calculate_reference_amount_when_temperature_between_30_and_40(self):
        self.fund_record.calculate_reference_amount(31)
        self.assertEqual(self.fund_record.reference_amount, 0)





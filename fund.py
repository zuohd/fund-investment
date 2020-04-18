import datetime


class FundRecord:
    def __init__(self, invest_amount=396):
        self.invest_amount = invest_amount
        self.create_data = datetime.date.today()
        self.fund_name = '中证红利'
        self.fund_code = '10032'
        self.index_temperature = 0
        self.left_amount = 0
        self.reference_amount = 0
        self.month_amount = 0

    def calculate_reference_amount(self, index_temperature):
        if index_temperature <= 10:
            self.reference_amount = self.invest_amount
        elif index_temperature <= 20:
            self.reference_amount = self.invest_amount * 0.8
        elif index_temperature <= 25:
            self.reference_amount = self.invest_amount * 0.6
        elif index_temperature <= 30:
            self.reference_amount = self.invest_amount * 0.5

    def calculate_month_amount(self):
        if self.index_temperature <= 10:
            return self.reference_amount + self.left_amount
        else:
            return self.reference_amount

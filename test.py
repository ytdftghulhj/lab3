import main.py
import pytest
import datetime as dt

@pytest.fixture
def cash_calculator():
  return main.CashCalculator()

def calory_calculator():
  return main.CaloriesCalculator()

def calculator():
  return main.Calculator()


def test_calory_calc(calory_calculator: main.CaloriesCalculator):
  length = len(calory_calculator.records)
  new_record = main.Record(amount=500, comment='шоколад')
  calory_calculator.add_record(new_record)
  assert len(calory_calculator.records) == length+1

def test_сash_calc(cash_calculator: main.CashCalculator):
  new_record = main.Record(amount=100000000, comment='на чай')
  cash_calculator.add_record(new_record)
  cash_calculator.get_today_cash_remained("rub")
  assert cash_calculator.text == "Денег нет, держись: твой долг "+ str(cash_calculator.remained/-1)+" "+ cash_calculator.currency

def test_record(record : main.Record):
  new_record = main.Record(amount=100, comment='чай')
  cash_calculator.add_record(new_record)
  assert cash_calculator.records[-1].date == dt.date.today()

def test_calculator(cash_calculator : main.CashCalculator):
  new_record = main.Record(amount=100, comment='чай')
  cash_calculator.add_record(new_record)
  cash_calculator.get_today_stats(self)
  assert calculator.today_amount != 0

 

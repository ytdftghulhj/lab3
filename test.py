import main
import pytest
import datetime as dt

def test_one():
    cash_calculator1 = main.CashCalculator(1000)
    length = len(cash_calculator1.records)
    new_record = main.Record(amount=500, comment='шоколад')
    cash_calculator1.add_record(new_record)
    assert len(cash_calculator1.records) == length + 1


def test_two():
    cash_calculator2 = main.CashCalculator(1000)
    new_record = main.Record(amount=100000000, comment='на чай')
    cash_calculator2.add_record(new_record)
    cash_calculator2.get_today_cash_remained("rub")
    assert cash_calculator2.text == "Денег нет, держись: твой долг " + str(
        cash_calculator2.remained / -1) + " " + cash_calculator2.currency


def test_three():
    cash_calculator3 = main.CashCalculator(1000)
    new_record = main.Record(amount=100, comment='чай')
    cash_calculator3.add_record(new_record)
    assert cash_calculator3.records[-1].date == dt.date.today()
#Возвращает False

def test_four():
    cash_calculator4 = main.CashCalculator(1000)
    new_record = main.Record(amount=100, comment='чай')
    cash_calculator4.add_record(new_record)
    cash_calculator4.get_today_stats()
    assert cash_calculator4.today_amount != 0


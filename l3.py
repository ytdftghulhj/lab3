import datetime as dt

class Record():
  def __init__(self, amount, comment, date=None):
    self.amount = float(amount)
    self.comment = comment
    if date is not None:
      self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
    else:
      self.date = dt.date.today

  def __str__(self):
    return f'количество {self.amount}, коментарий {self.comment} дата {self.date}'


class Calculator():
  def __init__(self,limit):
    self.limit = limit
    self.records = []
    self.text =""
    self.today_amount=0
  
  def add_record(self,new_record):
    self.records.append(new_record)
  
  def get_today_stats(self):
    today=dt.date.today
    for record in self.records:
      if record.date == today:
        self.today_amount += record.amount
    return self.today_amount
  
  def get_week_stats(self):
    today = dt.date.today
    date7 = today - dt.timedelta(days=7)
    week_amount=0
    for record in self.records:
      if record.date >= today and Record.date <= date7:
        week_amount += record.amount
    return week_amount
    
USD_RATE = 60.03
EURO_RATE = 59.87

class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
      remained = self.limit - self.get_today_stats()
      if currency == "eur":
        remained = remained/EURO_RATE
      elif currency == "usd":
        remained = remained/USD_RATE
      if remained > 0:
        self.text="У вас осталось еще " + str(remained)+" "+ currency
      elif remained < 0:
        self.text= "Денег нет, держись: твой долг "+ str(remained/-1)+" "+ currency
      else:
        self.text="Денег нет, держись"
      return self.text
      
      


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
      remained = self.limit - self.get_today_stats()
      return remained
      

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))

print(cash_calculator.get_today_cash_remained("rub"))

from datetime import date,datetime,timedelta

day_ = input("Day:")
month_ = input("Month: ")
year_ = input("Year: ")

def calc_age():
    date_ = year_+"-"+month_+"-"+day_
    date_ = datetime.strptime(date)

    if date> date.today():
        pass
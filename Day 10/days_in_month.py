
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month():
    month_days = [31,28,31,30,31,31,31,30]


year = int(input("Enter a year:\n"))
month = int(input("Enter a month:\n"))
days_in_month(year, month)
# print(days)
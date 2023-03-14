DAY_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
DAY_IN_YEAR = 365

def days(date: str) -> int:
    date_split = date.split("-")
    year = int(date_split[0]) * DAY_IN_YEAR
    month = int(date_split[1])-1
    days_in_month = list(DAY_IN_MONTH.values())[:month]
    return (year + sum(days_in_month) + int(date_split[2]))

print(abs(days("2019-06-29") - days("2019-06-30"))) # 1
print(abs(days("2020-01-15") - days("2019-12-31"))) # 15

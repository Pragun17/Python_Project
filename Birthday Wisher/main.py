# import smtplib
#
# my_email = "akashtiwari1711@yahoo.com"
# password = "ugthfykdvihnnrxk"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="akashtiwari017011@gmail.com", msg="Subject:Test email\n\nThis is a python generated email")

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
#
# date_of_birth = dt.datetime(year=2000, month=11, day=17)
# print(date_of_birth)
#
# age_year = now.year - date_of_birth.year
# print(f"Your age is {age_year} years")

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
current_day = now.weekday()

with open("quotes.txt") as quotes:
    today_quote = quotes.readlines()

quote_num = random.randint(0, len(today_quote) + 1)

my_email = "akashtiwari017011@gmail.com"
password = "Pragun17*"


if current_day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="akashtiwari1711@yahoo.com", msg=f"Subject:Todays quote\n\n{today_quote[quote_num]}")








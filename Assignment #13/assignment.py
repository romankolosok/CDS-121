import time
import datetime

#first

str_symb = "für die È gesamte Bevölkerung È quanto È qualità della"

print(str_symb, f"Length: {len(str_symb)}")
print(str_symb.encode('utf-8'), f"Byte length: {len(str_symb.encode('utf-8'))}")
with open("text.txt", "w") as f:
    f.write(str_symb)

ascii_str = str_symb.encode('ascii', 'replace')
print(ascii_str)

#second

user_date_str = input("Enter your birthday in MM/DD/YYYY format: ")
user_date = time.strptime(user_date_str, "%m/%d/%Y")
# print(user_date, time.mktime(user_date))
now = time.time()
print("Days from your birthday:", datetime.timedelta(seconds=now-time.mktime(user_date)))

#third

with open("input.txt") as f:
    dates = [datetime.datetime.strptime(line.strip(), "%Y-%m-%d") for line in f.readlines() if line.strip() != ""]

max = datetime.timedelta(days=0)
for i in range(1,len(dates)):
    if dates[i]-dates[i-1] > max:
        max = dates[i]-dates[i-1]

print(f"Biggest date gap is: {max.days} day(s)")
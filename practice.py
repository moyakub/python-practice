""" # Shift + option + A to comment/uncomment multiple lines
############  print name 


first_name = "Mohammad"
last_name = "Yakub"
full_name = f'your full name is {first_name} {last_name}'
print(full_name)



############  print name after user input

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = f'your full name is {first_name} {last_name}'
print(full_name)



############   Addition calculator
fist_number = input("Please enter first number: ");
second_number = input("Please enter second number: ");
total =  float(fist_number) + float(second_number);
print(f'Total is {total}'); """


""" #Current Datetime
from datetime import datetime

###########    output current locat date time
current_datetime = datetime.now();
print(f'Current Datetime is: {current_datetime}')

##########     output current UTC date time
current_utc = datetime.utcnow();
print(f'Current UTC time is: {current_utc}') """


##########      find birthday, week before birhtday.

""" from datetime import datetime, timedelta


birthday = input("When is your birhday (dd/mm/yy): ")
birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
one_week = timedelta(weeks=1)
one_week_before_birthday = birthday_date - one_week;

print(f'Your birthday date is: {birthday_date}'); 
print(f'A week before your birthday was: {one_week_before_birthday}');  """



""" ######## try except finally
x = 42
y = 0

try:
  result = x/y
except ZeroDivisionError as e:
  print("Cannot divide by 0")
else:
  print(f'result is: {result}')
finally:
  print("cleanup code")    
print("application still running")   """

print("new")
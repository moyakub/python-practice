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



""" ######## Error Handling try except finally
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

########### conditional Logic

""" price = 0.5;
if price > 1:
  print("Taxed")
else:
  print("Not Taxed") """
  

### multiple conditions  
""" 
country = input("Whats your country? ")
tax_rate = 0

#if country == "ca" or country == 'gbp':
if country in("ca","gbp","usa"):
  tax_rate = .07
elif country == "bd":
  tax_rate = .05  
else: 
  tax_rate = .15  




tax_rate_percentage = tax_rate * 100

format_tax_rate_percentage = "{:.2f}".format(tax_rate_percentage)


print(f'Please pay {format_tax_rate_percentage}% Tax') """ 


######### collection - items


""" 

names = ["Mohammad", "Ayyash"]
print(names[0]) """

########## Dictionaries
""" 

name1 = {}
name1["first"] = "Mohammad"
name1["last"] = "Yakub"

name2 = {}
name2["first"] = "Mohammad"
name2["last"] = "Yakub"

print(name1) 
print(name2) """

##### For/While Loop


name = ["Mohammad", "Yakub"]

for person in name:
  print(person)

index = 0
while index < len(name):
  print(name[index])
  index = index + 1
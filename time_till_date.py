import datetime

user_input = input(" Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() /60/60 )  #time converted into hours

print(f" Dear user! Time remaining for your goal is {goal} is {int(hours_till )} hours")

# if you want in days " Remove 12 line and in Add in 14 line as {time_till.days} in the place of int(hours_till)

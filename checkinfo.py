#Josiah N Savage 2/12/18
import time


while True:
    hourly_rate = float(input("What is your hourly rate?: "))
    question1 = input("Do you know the total number of hours worked?: ").lower()
    if question1 == "y" or question1 == "yes":
        hours_worked = float(input("How many hours have you worked?: ").lower())

        total_money = hours_worked * hourly_rate

        print("Your check should be {} before taxes".format(total_money))
    elif question1 == "n" or question1 == "no":

        how_many = float(input("How many days had the same hour schedule?: ").lower())

        what_hours = float(input("How many hours were in those days?: ").lower())

        diff_hour_days = float(input("How many days had different hours?: ").lower())

        other_hours = float(input("What were the total hours of the different hour schedule days?: ").lower())
    
        

        a = how_many * what_hours

        b = diff_hour_days * other_hours

        c = a + b

        total_money = hourly_rate * c

        print("Your check should be {} before taxes".format(total_money))
        
    
    
    



    again = input("Would you like to calculate more checks?: ").lower()

    if again == "y":
        continue
    elif again == "n":
        print("Thanks for using the check calculator! See you next time!")
        print("Check calulator exiting...")
        time.sleep(3)
        break

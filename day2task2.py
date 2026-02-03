total_bill_amount = float(input("enter the total amount spent in restaurant"))
number_of_people = input("enter number of people to split the bill")
bill_per_person = float(total_bill_amount) / int(number_of_people)
print("each person should pay:", bill_per_person)
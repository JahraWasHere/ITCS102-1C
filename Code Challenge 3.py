name = input("What's your name? ")
age = input("How old are you? ")
fare = eval(input("How much is your fare fee? "))
student = input("Are you a student? ")

discount = fare * 0.2
new_fare = fare - discount

if student.lower() == "yes" :
	print("Since you are a student, You have been given a 20% discount on your fare fee!")
	print("\nYour fee will now be", new_fare,"!")

else:
	print("Sorry! But your fee will remain as the regular price")

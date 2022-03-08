score = int(input("Please enter the student's score. "))
 
if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
elif score >= 80:
    print("This student's score of " + str(score) + " is a B.")
elif score >= 70:
    print("This student's score of " + str(score) + " is a C.")
elif score >= 60:
    print("This student's score of " + str(score) + " is a D.")
else:
    print("This student's score of " + str(score) + " is a F.")
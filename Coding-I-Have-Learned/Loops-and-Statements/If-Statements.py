# ############################
# Zachary Roberts
# Weather conditional statement
# ############################

temp = (int(input("what is the current temperature? ")))
raining = input("is it raining? [y or n]: ")




if (temp <= 50):
    print("it's cold out. probably should bring a jacket.")
    
if (raining == 'y' or raining == 'y'):
    print("don't forget to bring an umbrella!")


# ############################
# Grading System
# ############################
num_classes = int(input("Enter the number of classes you are taking: "))
for i in range(int(num_classes)):
    score = int(input("Enter your score for each of your individual classes(0-100): "))

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    if score >= 70:
        print("Passing")
    else:
        print("Failing")


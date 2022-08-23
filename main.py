user_gender = input("Pick one: Male or Female: ")
gender = user_gender.upper()

while not(gender == "MALE" or gender == "FEMALE"):
    user_gender = input("Pick one: Male or Female: ")

user_age = int(input("Your age: "))

user_weight = int(input("What's your weight on kg: "))

user_height = int(input("What's your height on cm: "))

user_activity = int(input("What's the level of your activity\n"
                          "Choose one of them:\n"
                          "1.Very active (hard exercise 6–7 days/week)\n"
                          "2.Active (exercise 6–7 days/week)\n"
                          "3.Moderately active (exercise 3–5 days/week)\n"
                          "4.Lightly active (exercise 1–3 days/week)\n"
                          "5.Sedentary (little or no exercise)\n"))

user_calories = 0

BMR = 0

if gender == "MALE":
    BMR = 66.47 + (13.75 * user_weight) + (5.003 * user_height) - (6.755 * user_age)

elif gender == "FEMALE":
    BMR = 655.1 + (9.563 * user_weight) + (1.850* user_height) - (4.676 * user_age)

if user_activity == 1:
    user_calories = BMR * 1.9

elif user_activity == 2:
    user_calories = BMR * 1.725

elif user_activity == 3:
    user_calories = BMR * 1.55

elif user_activity == 4:
    user_calories = BMR * 1.375

else:
    user_calories = BMR * 1.2

change = input("Do you want to lose or gain weight? ")
change_upper = change.upper()
while change_upper not in ["LOSE", "GAIN"]:
    change = input("Do you want to lose or gain weight? ")

if change_upper == "LOSE":
    print("You need to do a calorie deficit.")
    user_calories -= 500

else:
    print("You need to do a calorie surplus.")
    user_calories += 500

print(int(user_calories))

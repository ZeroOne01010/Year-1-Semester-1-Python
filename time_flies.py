# programme to output the following :-
#• their current age.
#• their age before their last Birthday.
#• their age after their next Birthday.

age = int(input("Please enter your age: "))

last_birthday = age - 1
next_birthday = age + 1

print(
    f"Your current age is {age}, on your last birthday you were {last_birthday} and on your next birthday you will be {next_birthday}."
)
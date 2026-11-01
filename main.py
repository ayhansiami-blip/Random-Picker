import random


items = []

while True:
    user_input = input("Give me some words(Separate them with \"&\" with no space): ")
    
    user_input = user_input.lower().strip().split("&")

    items = user_input


    for item in items:
        if len(item) > 75:
            print("Your input most be less then 75 charaters")
            
            continue

    else:
        print(random.choice(items))
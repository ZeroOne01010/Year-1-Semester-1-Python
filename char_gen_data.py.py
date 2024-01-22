import random
import json
import pandas as pd

def generate_attributes():#function to randomly generate attributes
    return {
        'Strength': random.randint(3, 18),
        'Intelligence': random.randint(3, 18),
        'Wisdom': random.randint(3, 18),
        'Dexterity': random.randint(3, 18),
        'Constitution': random.randint(3, 18),
    }
with open('/Users/jamiecarson/Library/CloudStorage/OneDrive-StaffordshireUniversity/SDAM/Week10/Beginner/char_classes.json', 'r') as file:
    data = json.load(file)

# Step 2: Extract data from JSON
table_data = []
classes = ["warrior", "wizard", "thief", "necromancer"]

for character_class in classes:
    stats = data.get(character_class, {})
    str_value = stats.get('str', '-')
    int_value = stats.get('int', '-')
    wis_value = stats.get('wis', '-')
    dex_value = stats.get('dex', '-')
    con_value = stats.get('con', '-')

    table_data.append([character_class, str_value, int_value, wis_value, dex_value, con_value])

# Step 3: Create a DataFrame using pandas
columns = ['Class', 'Str', 'Int', 'Wis', 'Dex', 'Con']
df = pd.DataFrame(table_data, columns=columns)

# Step 4: Display or save the table
print('Hello adventurer, below is the minimum stats required for each class')
print(df)

# Optional: Save DataFrame to a CSV file
df.to_csv('output_table.csv', index=False)



def print_attributes(attributes):#function to print current attributes
    for attribute, value in attributes.items():
        print(f"{attribute}: {value}")

def pick_a_class():#fucntion to pick a class 
    classes = {
        '1': 'Warrior',
        '2': 'Wizard',
        '3': 'Thief',
        '4': 'Necromancer'
    }
    
    print("\nSelect your class:")
    for key, value in classes.items():
        print(f"{key}. {value}")
    
    class_choice = input("Enter the number of your chosen class: ")
    return classes.get(class_choice)

def check_attributes(attributes, char_class):#function for checking minimum against required stats
    min_scores = {
        'Warrior': {'Strength': 15, 'Dexterity': 12, 'Constitution': 10},
        'Wizard': {'Intelligence': 15, 'Wisdom': 10, 'Dexterity': 10},
        'Thief': {'Strength': 10, 'Intelligence': 9, 'Dexterity': 15},
        'Necromancer': {'Strength': 10, 'Intelligence': 10, 'Wisdom': 15}
    }
    
    deficits = {}
    for attribute, value in min_scores[char_class].items():
        deficit = value - attributes[attribute]
        if deficit > 0:
            deficits[attribute] = deficit
    
    return deficits

def get_valid_points(total_points):#fucntion to check which points you can take and how many 
    while True:
        points_to_exchange = int(input())
        if points_to_exchange > 2 and points_to_exchange % 2 == 0 and points_to_exchange <= total_points:
            return points_to_exchange
        else:
            print(f"Invalid input. Enter an even number greater than 2 and less than or equal to {total_points}.")

def swap_points(attributes, deficits, char_class):#fucntion to swap points between attributes
    total_points = sum(deficits.values()) * 2
    
    while total_points > 0:
        print("\nCurrent attributes:")
        print_attributes(attributes)
        
        print("\nDeficit attributes:")
        print_attributes(deficits)
        
        print(f"\nYou have {total_points} points to exchange.")
        
        attribute_to_sacrifice = input("Select an attribute to sacrifice (or type 'done' to finish): ")
        if attribute_to_sacrifice.lower() == 'done':
            print("\nCharacter creation canceled. Restart the process from the beginning.")
            return None
        
        if attribute_to_sacrifice in attributes and attribute_to_sacrifice not in deficits:
            print("Enter the amount of points to exchange (even number greater than 2): ")
            points_to_exchange = get_valid_points(total_points)
            
            attribute_to_assign = input(f"Select an attribute to assign {points_to_exchange} points to: ")
            
            if attribute_to_assign in deficits:
                attributes[attribute_to_sacrifice] -= points_to_exchange
                attributes[attribute_to_assign] += points_to_exchange * 2
                total_points -= points_to_exchange * 2
                
                attributes[attribute_to_sacrifice] = max(attributes[attribute_to_sacrifice], 3)
                attributes[attribute_to_assign] = max(attributes[attribute_to_assign], 3)
                
                deficits = check_attributes(attributes, char_class)
                total_points = sum(deficits.values()) * 2
            else:
                print("Invalid selection. Try again.")
        else:
            print("Invalid selection. Try again.")
    
    return attributes

def main():#running the main program 
    print("Welcome to Character Generation!")

    player_attributes = generate_attributes()
    print("\nInitial attributes:")
    print_attributes(player_attributes)

    char_class = pick_a_class()

    if deficits := check_attributes(player_attributes, char_class):
        print(f"\nYour initial attributes do not meet the minimum scores for {char_class}.")
        print("You can exchange points from non-required attributes to meet the deficits.")

        player_attributes = swap_points(player_attributes, deficits, char_class)

        if player_attributes is not None:
            print(f'Final attributes\nCharacter creation successful! You are a {char_class}.')
            print_attributes(player_attributes)

    else:
        print(f'Your initial attributes now meet the required scores for {char_class}.\nCharacter creation has been successful, you are now ready for adventure !!')

if __name__ == "__main__":
    main()

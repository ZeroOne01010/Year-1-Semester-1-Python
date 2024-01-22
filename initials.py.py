def format_initials(full_name):
    # Remove extra spaces and split the name
    name_parts = full_name.strip().replace('  ', ' ').split()

    # Format initials based on the first character of each part
    formatted_initials = '-'.join([part[0].upper() for part in name_parts])

    return formatted_initials

# Prompt the user for input
user_input = input('Please enter your full name: ')

# Get and print the formatted initials
formatted_initials = format_initials(user_input)
print('Initials output:', formatted_initials)

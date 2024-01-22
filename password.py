#Password to be stored and take user input to match pass word 

password = str(input('Please create a password')).lower()

user_input_password = str(input('Please enter your password:')).lower()

if user_input_password == password:
    print('Welcome, that is the correct password')
else:
    print('Incorrect password')
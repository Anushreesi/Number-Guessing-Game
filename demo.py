import random

num = random.randint(0, 10)
print(f'''
---------------------------
Correct answer: {num}
---------------------------
''')

attempt = 4
msg = ''
while attempt > 0:
   
    user_input = int(input('Enter the Number: '))
    if user_input == num:
        msg = 'You Won the round!'
        break
    elif user_input > num:
        print(f'{user_input} is greater.\nRemaining attempts are: {attempt}.')
        attempt -= 1
        

    elif user_input < num:
        print(f'{user_input} is smaller.\nRemaining attempts are: {attempt}.')
        attempt -= 1

    else:
        print('Something went wrong!')
        break
    
print(msg)
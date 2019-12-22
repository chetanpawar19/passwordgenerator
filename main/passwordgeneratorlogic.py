import  random

def passwordgeneration(no_of_passwords, password_length, user_combinations):
    '''the function takes argument as required user combination like uppercase, lowercase, digits and password length. it returns randomly generated password'''

    digits_choice = '0123456789'
    alpha_uppercase_choice = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_lowercase_choice = 'abcdefghijklmnopqrstuvwxyz'
    special_char_choice = '!@#$%^&*()'

    combination_dict= {}
    password_list=[]
    iterations_per_combination = password_length//len(user_combinations)    #12 length/ 4 combination selected = 3 iteratons each
    remaining_iterations =  password_length % len(user_combinations)

    for user_combination in user_combinations:
        if user_combination == 'uppercase_letters':
            combination_dict['ABCDEFGHIJKLMNOPQRSTUVWXYZ']=iterations_per_combination
        elif user_combination == 'lowercase_letters':
            combination_dict['abcdefghijklmnopqrstuvwxyz'] = iterations_per_combination
        elif user_combination == 'digits':
            combination_dict['0123456789'] = iterations_per_combination
        elif user_combination == 'special_characters':
            combination_dict['!@#$%^&*()']=iterations_per_combination
        else:
            pass

    temp1=[]
    for paswordno in range(no_of_passwords):
        password=''
        for key,value in combination_dict.items():
            for i in range(0,int(value)):
                password=password+random.choice(str(key))
        #for handling remainging iterations 15%4 = 3
        for itr in range(remaining_iterations):
            password=password+random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()")
        temp1 =list(password)
        random.shuffle(temp1)
        password = ''.join(temp1)
        password_list.append(password)

    return password_list





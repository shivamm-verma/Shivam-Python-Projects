f = open("passwords file.txt","a+")           # file opening for checking before genrating a password whether if it was already created or not


"""
# this program would create random passwords of length = 8 each
# NONE OF PASSWORDS WOULD BE COMMON/SAME
# AUTHOR: SHIVAM VERMA, student (@ escorts wrold school,kanpur)

"""


def PasswordGenrator():            # function that would create random password
    import random
    list_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',\
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']              
    list_num = [1,2,3,4,5,6,7,8,9,0]                                            
    list_special = ['~','@','#','$','%','&','*','?','/',' '] 
    list_all = list_alpha + list_num + list_special     # list of all possible pass elements

    passw = list()
    passw_elem, passw_len = 0, 1

    while passw_len <= 8:
        str_case = random.randint(0,1)     #0= lower case, 1 = upper case
        passw_elem = random.choice(list_all)
        if passw_elem in list_alpha:
            if str_case == 1:
                passw_elem = passw_elem.upper()

        if passw_len == 1:
            if (passw_elem in list_num) or (passw_elem in list_special):
                passw_elem = random.choice(list_alpha) 

        passw.append(passw_elem)
        passw_len += 1

    passw_lst = list()
    for i in passw:
        str_i = str(i)
        passw_lst.append(str_i)

    password = "".join(passw_lst)
  #  print("Your Random password is: ",password)
    return password


def VariablePassword():                      # function that would let there should be no same passwords
    f = open("passwords file.txt","a+")
    variable_pass = PasswordGenrator()

    f.write(str(variable_pass))
    f.write("\n")
    f.write("\n")

    data_file = f.read()

    for i in data_file:
        if i == variable_pass:                    # NO SAME PASSWORDS SHOULD BE EXISTED SO THAT NO USER COULD HAVE SAME SET OF PASSWORD
            print("We gave you a same password between you and another user, new password is: ")
            variable_pass = PasswordGenrator()
            print(f"Your Password: {variable_pass}")
            
    print(f"Your Password: {variable_pass}")

def how_many_times_same_password():
    f = open("passwords file.txt","r")
    data = f.readlines()
    count = 0
    for i in data:
        if i == "We gave you a same password between you and another user, new password is: ":
            count += 1
    print(f"Total Number of times when we assigned you same password is: {count}")

def password_starting_from(alpha):
    alpha = str(alpha)
    alpha_upp = alpha.upper()
    list_searched = []
    f = open("passwords file.txt","r")
    data = f.readlines()
    for i in data:
        if i != "n":
            i = str(i)
            if i.startswith(alpha) or (i.startswith(alpha_upp)) or (i.startswith(alpha.swapcase()))  == True:
                list_searched.append(i)
    print(f"List of passwords starting from {alpha} are: ")
    print(list_searched)

if __name__ == "__main__":          # all testing and other stuffs here, to make this file as a Module/Library
    pass
   # VariablePassword()
   # how_many_times_same_password()
   # password_starting_from("ren")


'''    a = PasswordGenrator()
    print(a)
    print(type(a))'''
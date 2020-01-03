def ValidatePassword(Pass):
    Index1 = 0
    Index2 = 0
    Index3 = 0
    for i in Pass:
        if 'a' <= i <= 'z':
            Index1 = Index1 + 1
        elif 'A' <= i <= 'Z':
            Index2 = Index2 + 1
        elif '0' <= i <= '9':
            Index3 = Index3 + 1
    if Index1 >= 2 and Index2 >= 2 and Index3 >= 3:
        return True
    else:
        return False
            
print('the password should contain:')
print('1. At least 2 lower-case alphabetic characters')
print('2. At least 2 upper-case alphabetic characters')
print('3. At least 3 numeric characters')
Password = input('Enter a password: ')
Judge = ValidatePassword(Password)
if Judge == True:
    print('Password is valid')
else:
    print('Password is invalid')
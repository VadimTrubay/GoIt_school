is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))
access = is_permission
if is_permission is True or False and is_active is True or False:
    access = True
print(access)
if is_permission is True and is_active is True:
    access = True
print(access)

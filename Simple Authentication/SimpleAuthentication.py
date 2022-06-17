import time
userPasswords= { 'Mel': 'Hello', 'Bob' : 'aaa', 'Alice': 'abc123', 'Anna' : 'goop', 'Dozer': 'Zion'}

accessGranted = False


while accessGranted== False:
    inName = input('please enter your username: ')
    if inName in  userPasswords:
        goodPassword = False
        while goodPassword== False:
            inPassword = input ('please enter your password: ')
            if inPassword == userPasswords[inName]:
                goodPassword = True
                accessGranted = True
                print('waiting .')
                time.sleep(1)
                print('waiting ...')
                time.sleep(1)
                print('waiting ...')
                time.sleep(1)
                print('ACCESS GRANTED')
            else:  # say invalid password
                print('that is not a valid password')
                print('waiting .')
                time.sleep(1)
                print('waiting ..')
                time.sleep(1)
                print('waiting ...')
                time.sleep(1)
    else: # say user name is invalid 
        print('that is not a valid username')

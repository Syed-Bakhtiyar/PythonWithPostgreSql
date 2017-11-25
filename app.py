from module import Module


def __main__():
    database = Module()
    choice = -1
    while True:
        if choice == 1 or choice == 2:
            break
        print('1.Sign Up \n2.Sign In\n')
        try:
            choice = int(input("Enter Your Choice: "))
        except Exception as e:
            print('Type Number Only')

    if choice == 1:
        check = True
        while check:
            email = input('Enter Email Address: ')
            first_name = input('Enter First Name: ')
            last_name = input('Enter Last Name: ')
            check = database.setUser(email, first_name, last_name)
            if check:
                choice = 2

    if choice == 2:
        check = True
        while True:
            email = input("Enter Your Email Address Or E To Exit: ")
            if len(email) == 0:
                print("Please Type Your Email Again or E to back: ")
            elif email == 'e' or email == "E":
                break
            else:
                id = database.getUser(email)
                if id != -1:
                    choice_for_write_read = 1
                    while choice_for_write_read:
                        choice_for_write_read = input("1.Post\n2.See Your Post\n3.See Others Post\n0.Back")
                        try:
                            choice_for_write_read = int(choice_for_write_read)
                        except Exception as e:
                            print(str(e))
                        else:
                            if choice_for_write_read == 1:
                                post = input("Write Some Thing You Want: ")
                                if (len(post) > 0):
                                    database.setPost(id, post)
                                else:
                                    print("Please Enter Some Thing You Want ")
                            elif choice_for_write_read == 2:
                                list = database.getCurrentUserPost(id)
                                if len(list) == 0:
                                    print("You Haven't Any Post")
                                else:
                                    for item in list:
                                        print('---------------------------')
                                        print(item['first_name'] + " " + item['last_name'] + "\n\t")
                                        print(item['post'])
                                        print('---------------------------')
                                        print("\n\n")
                            elif choice_for_write_read == 3:
                                list = database.getAnotherUserPost(id)
                                if len(list) == 0:
                                    print("You Haven't Any Post")
                                else:
                                    for item in list:
                                        print('---------------------------')
                                        print(item['first_name'] + " " + item['last_name'] + "\n\t")
                                        print(item['post'])
                                        print('---------------------------')
                                        print("\n\n")
                            else:
                                break

                    else:
                        print('Please Enter Correct Email Address Or Create Your Account')


__main__()

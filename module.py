from database import connection


class Module:
    # For Create User

    def setUser(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        try:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (email,first_name,last_name) VALUES (%s, %s, %s )',
                               (self.email, self.first_name, self.last_name))
                connection.commit()
        except Exception as e:
            print("This User Is Already Exist\nEnter Again\n--------------------")
            return True
        else:
            print('User Created Successfully')
            return False

    # For Get User


    def getUser(self, email):

        id = -1
        try:
            with connection.cursor() as cursor:
                cursor.execute("Select id from users where email = '" + email + "'")
                result = cursor.fetchall()
                for row in result:
                    id = row[0]
                    print(str(id))

        except Exception as e:
            print("User Not Found " + str(e))
            return id
        else:
            return id

    def setPost(self, id, post):
        with connection.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO post (user_id,post) VALUES (%s,%s)', (id, post))
                connection.commit()
            except Exception as e:
                print(str(e))

            else:
                print('Posted Successfully')

    def getCurrentUserPost(self, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT u.first_name, u.last_name, p.post FROM users u INNER JOIN post p "
                           "ON u.id = p.user_id WHERE u.id = " + str(id))
            result = cursor.fetchall()
            data = list()
            for row in result:
                user_name = row[0]
                user_last_name = row[1]
                user_post = row[2]
                data.append({'first_name': user_name, 'last_name': user_last_name, 'post': user_post})

            return data

    def getAnotherUserPost(self, id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT u.first_name, u.last_name, p.post FROM users u INNER JOIN post p "
                           "ON u.id = p.user_id WHERE u.id != " + str(id))
            result = cursor.fetchall()
            data = list()
            for row in result:
                user_name = row[0]
                user_last_name = row[1]
                user_post = row[2]
                data.append({'first_name': user_name, 'last_name': user_last_name, 'post': user_post})

            return data

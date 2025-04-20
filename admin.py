class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f'User {user.get_name()} added successfully.')
        else:
            print('Only User instances can be added.')

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f'User {user.get_name()} removed successfully.')
                return
        print('User not found.')

    def list_users(self):
        if not self.__users:
            print('No users found.')
        else:
            print('List of users:')
            for user in self.__users:
                print(f'ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')



if __name__ == "__main__":
    admin = Admin(1, 'Admin User')
    user1 = User(2,'Светлана' )
    user2 = User(3, 'Екатерина')

    admin.add_user(user1)
    admin.add_user(user2)
    admin.list_users()

    admin.remove_user(2)
    admin.list_users()
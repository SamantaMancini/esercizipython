class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserView:
    def display_user_details(self, user):
        print(f"Nome: {user.name}")
        print(f"Email: {user.email}")

class UserController:
    def __init__(self, user, view):
        self.user = user
        self.view = view

    def update_user_details(self, name, email):
        self.user.name = name
        self.user.email = email

    def display_user_details(self):
        self.view.display_user_details(self.user)

user = User("Alice", "alice@example.com")
view = UserView()
controller = UserController(user, view)

controller.display_user_details()
controller.update_user_details("Alice Smith", "alice.smith@example.com")
controller.display_user_details()
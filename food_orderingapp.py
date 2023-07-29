class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class AdminLogin:
    def __init__(self):
        self.admin = Admin("admin_username", "admin_password")       # Set your admin credentials here

    def login(self, username, password):
        if username == self.admin.username and password == self.admin.password:
            print("Admin login successful!")
            # Redirect to the admin panel/dashboard
        else:
            print("Invalid admin credentials!")

class UserLogin:
    def __init__(self):
        self.users = []  # Store registered users in this list

    def register(self, full_name, phone_number, email, address, password):
        # Check if the user already exists
        for user in self.users:
            if user.email == email:
                print("User already exists!")
                return

        new_user = User(full_name, phone_number, email, address, password)
        self.users.append(new_user)
        print("User registered successfully!")
        # Redirect to the user login screen

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print("User login successful!")
                # Redirect to the user profile/dashboard
                return

        print("Invalid email or password!")

class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class AdminPanel:
    def __init__(self):
        self.food_items = []  # Store food items in this list
        self.current_food_id = 1

    def generate_food_id(self):
        food_id = self.current_food_id
        self.current_food_id += 1
        return food_id

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = self.generate_food_id()
        new_food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(new_food_item)
        print("Food item added successfully!")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated successfully!")
                return

        print("Food item not found!")

    def view_food_items(self):
        if not self.food_items:
            print("No food items available.")
            return

        print("List of Food Items:")
        for food_item in self.food_items:
            print("Food ID:", food_item.food_id)
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return

        print("Food item not found!")

# Admin functionalities
admin_panel = AdminPanel()

admin_panel.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin_panel.add_food_item("Vegan Burger", "1 piece", 320, 5, 8)
admin_panel.add_food_item("Truffle Cake", "500gm", 900, 0, 2)

admin_panel.view_food_items()

admin_panel.edit_food_item(2, "Vegan Burger Deluxe", "1 piece", 350, 5, 8)

admin_panel.view_food_items()

admin_panel.remove_food_item(3)

admin_panel.view_food_items()


class User(Admin):
    def __init__(self, username, password):
        # Call the super class (Admin) constructor
        super().__init__(username, password)
        self.order_history = []
        self.full_name = ""
        self.phone_number = ""
        self.email = ""
        self.address = ""

    def get_selected_food_items(self, selected_item_ids):
        selected_food_items = []
        for food_item in admin_panel.food_items:
            if food_item.food_id in selected_item_ids:
                selected_food_items.append(food_item)
        return selected_food_items



    def create_order(self, selected_food_items):
        return selected_food_items


    def place_new_order(self):
        # Display the list of available food items
        print("Available Food Items:")
        for food_item in admin_panel.food_items:
            print(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

        # Prompt the user to select food items
        selected_items = input("Select food items (enter item numbers separated by commas): ")
        selected_items = [int(item) for item in selected_items.split(',')]

        # Get the selected food items
        selected_food_items = self.get_selected_food_items(selected_items)

        # Display the selected food items for review
        print("Selected Items:")
        for food_item in selected_food_items:
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: INR {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print()

        # Prompt the user to confirm the order
        confirmation = input("Confirm the order? (Y/N): ")

        if confirmation.lower() == "y":
            # Place the order
            order = self.create_order(selected_food_items)

            # Add the order to the user's order history
            self.add_order_to_history(order)

    def add_order_to_history(self, order):
        self.order_history.append(order)


    def view_order_history(self):
        if not self.order_history:
            print("No order history available.")
            return

        print("Order History:")
        for order in self.order_history:
            for food_item in order:
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: INR {food_item.price}")
                print(f"Discount: {food_item.discount}")
                print()

    def update_profile(self):
        # Prompt the user to enter updated profile information
        full_name = input("Enter full name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        password = input("Enter new password: ")

        # Update the user's profile information
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

        # Save the updated profile details
        self.save_profile_details()

    def save_profile_details(self):
        # Save the user's profile details to the database or file
        # Implementation details depend on your application architecture
        pass



user = User("user", "user_password")
user.place_new_order()
print('Order Placed Successfully')
user.view_order_history()
user.update_profile()

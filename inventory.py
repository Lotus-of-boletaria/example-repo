
# ========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        def get_cost(self):
            return self.cost

        def get_quantity(self):
            return self.quantity

        def __str__(self):
            return (f"{self.country}{self.code}{self.product}"
                    f"{self.cost}{self.quantity}")


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents data to create one object of shoes. You must use the try-except
    in this function for error handling. Remember to skip the first line using
    your code.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skipping first line.
            for line in file:
                line_attributes = line.strip().split(',')
                # Append object to the list.
                object = Shoe(line_attributes[0], line_attributes[1],
                              line_attributes[2], line_attributes[3],
                              line_attributes[4])
                shoe_list.append(object)

    except FileNotFoundError:  # Incase of missing file.
        print("Error: 'inventory.txt' not found.")

    return shoe_list


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:  # Asking user for information required for new shoe object.
        new_shoe_product = input("Please enter Product name: ")
        new_Shoe_country = input("Please enter country of origin: ")
        new_shoe_code = input("Please enter Product code: ")
        new_shoe_cost = int(input("Please enter Product cost: "))
        new_shoe_qty = int(input("Please enter Product quantity: "))
        # Creating new object.
        new_shoe = Shoe(new_Shoe_country, new_shoe_code, new_shoe_product,
                        new_shoe_cost, new_shoe_qty)
        # Adding new shoe to list.
        shoe_list.append(new_shoe)

    except ValueError:  # Incase of invalid input.
        print("Error: invalid value entered, please try again.")
        capture_shoes()


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Loop that prints all shoes in the list in a way thats easy
    # to read.
    for i in range(len(shoe_list)):
        print(f"[{i+1}] {shoe_list[i].product}\n"
              f"Country:  {shoe_list[i].country}\n"
              f"Code:     {shoe_list[i].code}\n"
              f"Price:    {shoe_list[i].cost}\n"
              f"Quantity: {shoe_list[i].quantity}\n")


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Getting the lowest quantity arrtibute from the shoe list.
    product_lowest_qty = min(int(shoe.quantity) for shoe in shoe_list)
    # Loop to show user the product with the lowest quantity.
    for index in range(len(shoe_list)):
        if int(shoe_list[index].quantity) == product_lowest_qty:
            print(f"Running low on product: {shoe_list[index].product}\n"
                  f"Current available stock: {shoe_list[index].quantity}")
            # Requesting user to confirm restock.
            restock_confirm = input("Would you like to restock? "
                                    "(Y/N): ").lower()
            if restock_confirm == "y":
                try:  # Getting amount of stock the user would like to add.
                    add_qty = int(input("Enter how many units you "
                                        "would like to order: "))
                    # Ading new order to current quantity.
                    shoe_list[index].quantity = (int(shoe_list[index].quantity)
                                                 + add_qty)
                    # Confirming restock success.
                    print(f"{shoe_list[index].product} Successfully restocked."
                          f"\nCurrent available stock: "
                          f"{shoe_list[index].quantity}")
                except ValueError:  # Incase of invalid input.
                    print("Error: Input was not a number.")
                    re_stock()

            elif restock_confirm == "n":
                print("Confirmed, not restocking ay this time.")

            else:  # Incase user enters invalid input.
                print("Please enter either 'Y' or 'N': ")
                re_stock()


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
     '''
    temp_list = []  # Temp list to store product information.
    # Asking user to input shoe code.
    shoe_code_input = input("\nPlease input serial code: ")
    # Loop to find information based on given code.
    for index in range(len(shoe_list)):
        if shoe_list[index].code == shoe_code_input:
            temp_list.append(f"\nProduct:  {shoe_list[index].product}")
            temp_list.append(f"Country:  {shoe_list[index].country}")
            temp_list.append(f"Price:    {shoe_list[index].cost}")
            temp_list.append(f"Quantity: {shoe_list[index].quantity}")
    if len(temp_list) != 0:
        print(*temp_list, sep="\n")  # Printing product information.
    else:
        # Incase of invalid input.
        print("\nError: Please enter valid serial number.")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Loop to calculate the total value for each item.
    for i in range(len(shoe_list)):
        print(f"\n[{i+1}] {shoe_list[i].product}\nTotal Value:  "
              f"{(int(shoe_list[i].cost) * int(shoe_list[i].quantity))}\n")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Determining the highest quantity attribute in the shoe list.
    product_highest_qty = max(int(shoe.quantity) for shoe in shoe_list)
    # Loop to find information based on highest quantity attribute.
    for index in range(len(shoe_list)):
        if int(shoe_list[index].quantity) == product_highest_qty:
            # Printing out information like the shoe is for sale.
            print(f"\nBUY NOW! The {shoe_list[index].product}\n"
                  f"For only {shoe_list[index].cost}!\n"
                  f"Available in store all accross {shoe_list[index].country}!"
                  "\n")


read_shoes_data()  # Calling function to read txt file.
# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


# Menu function.
def calc_app():
    while True:
        print("\nInventory App Menu")
        print("1. View All")
        print("2. Search Shoe")
        print("3. Value per item")
        print("4. Highest Quantity")
        print("5. Capture Shoes")
        print("6. Restock")
        print("7. Exit")
        choice = input("Enter your choice (1 - 7): ")

        # Call functions based on user choice.
        if choice == '1':
            view_all()
        elif choice == '2':
            search_shoe()
        elif choice == '3':
            value_per_item()
        elif choice == '4':
            highest_qty()
        elif choice == '5':
            capture_shoes()
        elif choice == '6':
            re_stock()
        elif choice == '7':
            print("\nThank you for using the Inventory App.\n")
            break  # Exit the loop, ending the program
        else:
            print("Error: invalid input. Please try again: ")


# Start the app
calc_app()

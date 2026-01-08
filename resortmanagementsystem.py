# Resort Management System

customer_name = ""
customer_phone = ""
room_rent = 0
food_bill = 0
total_bill = 0

def customer_details():
    global customer_name, customer_phone
    customer_name = input("Enter customer name: ")
    customer_phone = input("Enter phone number: ")
    print("\nCustomer details saved successfully!\n")

def room_booking():
    global room_rent
    print("\nRoom Types:")
    print("1. Standard Room - Rs.2000/day")
    print("2. Deluxe Room   - Rs.3500/day")
    print("3. Suite Room    - Rs.5000/day")

    choice = int(input("Enter room choice: "))
    days = int(input("Number of days: "))

    if choice == 1:
        room_rent = 2000 * days
    elif choice == 2:
        room_rent = 3500 * days
    elif choice == 3:
        room_rent = 5000 * days
    else:
        print("Invalid choice")
        room_rent = 0

    print(f"Room booked successfully! Room rent: Rs.{room_rent}\n")

def food_order():
    global food_bill
    print("\nFood Menu:")
    print("1. Breakfast - Rs.200")
    print("2. Lunch     - Rs.400")
    print("3. Dinner    - Rs.500")

    choice = int(input("Enter food choice: "))
    quantity = int(input("Enter quantity: "))

    if choice == 1:
        food_bill += 200 * quantity
    elif choice == 2:
        food_bill += 400 * quantity
    elif choice == 3:
        food_bill += 500 * quantity
    else:
        print("Invalid choice")

    print(f"Food order added! Food bill: Rs.{food_bill}\n")

def billing():
    global total_bill
    total_bill = room_rent + food_bill
    print("\n------ BILL DETAILS ------")
    print("Customer Name :", customer_name)
    print("Phone Number  :", customer_phone)
    print("Room Rent     : Rs.", room_rent)
    print("Food Charges  : Rs.", food_bill)
    print("--------------------------")
    print("Total Bill    : Rs.", total_bill)
    print("--------------------------\n")

while True:
    print("====== RESORT MANAGEMENT SYSTEM ======")
    print("1. Enter Customer Details")
    print("2. Room Booking")
    print("3. Order Food")
    print("4. Generate Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_details()
    elif choice == 2:
        room_booking()
    elif choice == 3:
        food_order()
    elif choice == 4:
        billing()
    elif choice == 5:
        print("Thank you for using Resort Management System!")
        break
    else:
        print("Invalid choice! Please try again.\n")


products = {
    "Milk": {
        "price": 250,
        "stock": 15
    },
    "Bread": {
        "price": 180,
        "stock": 20
    },
    "Eggs": {
        "price": 320,
        "stock": 10
    },
    "Rice": {
        "price": 450,
        "stock": 8
    },
    "Sugar": {
        "price": 170,
        "stock": 12
    },
    "Tea": {
        "price": 950,
        "stock": 5
    },
    "Cooking Oil": {
        "price": 680,
        "stock": 7
    },
    "Salt": {
        "price": 60,
        "stock": 25
    },
    "Chicken": {
        "price": 750,
        "stock": 6
    },
    "Juice": {
        "price": 220,
        "stock": 18
    }
}

cart = {}
choice = 0

while(choice != 6):
    print("\n- - - GROCERY STORE - - -\n")
    print("1. View Products")
    print("2. Buy Product")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. Exit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print(15 * "- ")
        print(f"{'Products': <15} {'Price': <5} {'Stock'}")
        print(15 * "- ")
        
        for product, data in products.items():
            print(f"{product: <15} {data['price']: <5} {data['stock']}")
        print(15 * "- ")

    elif choice == 2:
        name = input("Enter the product name: ").strip().title()
        quantity = int(input("Enter the Quantity: "))

        if name in cart and name in products:
            while(quantity > products[name]['stock']):
                print(f"This product stock is {products[name]['stock']}")
                quantity = int(input("Enter again or zero if don't want: "))

            cart[name][0] += quantity
            products[name]['stock'] -= quantity
            print(f"{quantity} '{name}' added to the cart successfully! ")


        elif name in products and products[name]['stock'] >= quantity:
            cart[name] = [quantity, products[name]['price']]
            
            products[name]['stock'] -= quantity
            print(f"{quantity} '{name}' added to the cart successfully! ")

        elif name in products:
            while(quantity > products[name]['stock']):
                print(f"This product stock is {products[name]['stock']}")
                quantity = int(input("Enter again or zero if don't want: "))
            
            cart[name] = [quantity, products[name]['price']]
            products[name]['stock'] -= quantity
            print(f"{quantity} '{name}' added to the cart successfully")

        else:
            print("Product doesn't available! ")

    elif choice == 3:
        print(15 * "- ")
        print(f"{'Products': <12} {'Quantity': <9} {'Price'}")
        print(15 * "- ")

        for item, data in cart.items():
            print(f"{item: <12} {data[0]: <9} {data[1]}")
        print(15 * "- ")

        if len(cart) == 0:
            print("There are no items in the cart yet! ")
    
    elif choice == 4:
        name = input("Enter the product name: ").strip().title()

        if name in cart:
            products[name]['stock'] += cart[name][0]
            cart.pop(name)
            print(f"'{name}' Removed from your cart successfully! ")
        else:
            print("Item not found in cart! ")

    elif choice == 5:
        total = 0
        for item in cart:
            total += (cart[item][0] * cart[item][1])

        print(15 * "- ")
        print(f"{'Products': <12} {'Quantity': <9} {'Price'}")
        print(15 * "- ")

        for item, data in cart.items():
            print(f"{item: <12} {data[0]: <9} {data[1]}")
        print(15 * "- ")

        print(f"{'Total':<12} {':': <9} {total}")

    elif choice == 6:
        print("Thank You for Shopping! ")
    else:
        print("You Entered wrong choice! ")

print("--------x--------")
print("pname || quantity")
print("-----------------")
product={"rice":50,"pulses":120,"oil":150,"salt":10,"soap":35,"sugar":65,"himalya facewash":139,"dishwash liquid":65,"bread":50,"rusk":35,"cashew":780,"almond":760}
stock={"rice":20,"pulses":20,"oil":10,"salt":25,"soap":24,"sugar":100,"himalya facewash":10,"dishwash liquid":12,"bread":50,"rusk":24,"cashew":10,"almond":10}
for name,quantity in stock.items():
    print(name,quantity)

print("-----------x-----------")
print("pname || Price")
print("-----------------------")

for name, price in product.items():
    print(name,'₹',price)
cart={}
def view_cart():
    print("-------- YOUR CART --------")

    if not cart:
        print("Cart is empty")
        return

    total = 0

    for name, quantity in cart.items():
        amount = quantity * product[name]
        print(name, quantity, "x", product[name], "=", amount)
        total += amount

    print("---------------------------")
    print("Current Total:", total)
n=input("enter your name:")

p=input("enter your mobile number:")
if len(p)==10:
    print(p)
else:
    print("incorrect mobile number")


while True:


    product_name=input("enter product----or -----'done' to finish----or-----'remove'to remove item into a cart----or----'view'to cart view").lower()
    if product_name=="done":
        break

    if product_name == "remove":
        remove_item = input("Enter item to remove: ").lower()

        if remove_item in cart:
            removed_quantity = cart.pop(remove_item)
            stock[remove_item] += removed_quantity
            print("Item removed from cart")
        else:
            print("Item is not in cart")

        continue
    if product_name=="view":
        view_cart()
        continue
    
    if product_name in product:
        while True:
            try:
                quantity = int(input("enter product quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0")
                else:
                    break

            except ValueError:
                print("Please enter a valid whole number")
        if quantity <=stock[product_name]:
            cart[product_name]=cart.get(product_name, 0) + quantity
            stock[product_name]-=quantity



            print("remaining stock",stock[product_name])
            print("product added to cart")
            amount=quantity*product[product_name]
            print(amount)
        else:
            print("sorry only ",stock[product_name],"stock available")

    else:
        print("product not available ")

print("\n-------- YOUR CART --------")

print("NAME:-",n)
if len(p)==10:
    print("mobile number:-",p)
else:
    print("incorrect mobile number")

print("------------xxxx-----------")


grand_total = 0

for name, quantity in cart.items():
    amount = quantity * product[name]
    print(name, quantity, "x", product[name], "=", amount)
    grand_total += amount

print("---------------------------")
print("Total",grand_total )

if grand_total>=5000:
    grant=grand_total*10/100
    grand_total-=grant
    print("-----------------------------")
    print("TOTAL:-",grand_total)
    print("-----------------------------")
    print("ENJOY , YOU GOT A 10% DISCOUNT....")
    print("======THANKYOU======")
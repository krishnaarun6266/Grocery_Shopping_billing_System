# Grocery shopping billing system
Project Statement
##	Problem Statement
Small grocery shopping processes require keeping track of product prices, available stock, selected quantities, cart contents, and the final bill. Manual handling of these tasks can sometimes lead to incorrect quantity selection or calculation errors.
The Grocery Shopping Cart System is a Python console application designed to simulate a basic grocery shopping workflow. It allows a user to select products, enter quantities, check stock availability, manage a shopping cart, and calculate the final bill.
The project applies Python Essential concepts to a practical real-world problem.
## Scope of the Project
The scope of this project includes:
•	Maintaining a list of grocery products and their prices.
•	Maintaining available stock quantities.
•	Displaying product and stock information.
•	Accepting customer name and mobile number.
•	Allowing users to add products to a shopping cart.
•	Validating product quantities.
•	Checking stock availability.
•	Allowing users to view the cart.
•	Allowing users to remove products from the cart.
•	Returning removed quantities to available stock.
•	Calculating item-wise amounts.
•	Calculating the total bill.
•	Applying a 10% discount when the bill is at least ₹5000.
•	Displaying the final amount and a thank-you message.
## Target Users
The target users of this project are:
•	Students learning Python programming.
•	Beginners practicing Python Essential concepts.
•	Users who want to simulate a basic grocery shopping process.
•	Teachers/evaluators reviewing the application of Python programming concepts to a real-world problem.
## High-Level Features
Product and Stock Management
•	Product names and prices are maintained using dictionaries.
•	Available product quantities are maintained using a stock dictionary.
•	Product and stock information can be displayed to the user.
Shopping Cart
•	Users can select products.
•	Users can enter the required quantity.
•	The program validates the quantity.
•	The program checks available stock.
•	Products are added to the cart.
•	The current cart can be viewed.
•	Products can be removed from the cart.
Billing
•	Item-wise amount is calculated using quantity × price.
•	The grand total is calculated.
•	A 10% discount is applied when the grand total is ₹5000 or more.
•	The final payable amount is displayed.
Input Validation
•	Invalid quantity input is handled.
•	Zero and negative quantities are rejected.
•	Insufficient stock is detected.
•	Invalid product names are rejected.
•	Mobile number length is checked.
## Main User Workflow
             Start
  	↓
Display Products & Stock
  	↓
Enter Customer Details
  	↓
Select Product
  	↓
Enter Quantity
  	↓
Validate Quantity
  	↓
Check Stock
  	↓
Add to Cart
 ↓
View / Remove / Continue Shopping
 ↓
Enter "done"
  	↓
Generate Bill
  	↓
Calculate Total
                 ↓
Check Discount Condition
                 ↓
Display Final Amount
                 ↓
End

## Python Concepts Used
The project uses concepts relevant to Python Essentials, including:
•	Variables
•	Strings
•	Dictionaries
•	Functions
•	for loops
•	while loops
•	Conditional statements
•	User input/output
•	Arithmetic operations
•	String methods
•	try-except exception handling
•	Basic input validation
## Major Functional Areas
The project is divided logically into three major functional areas:
1.	Product and Stock Management
2.	Shopping Cart Management
3.	Billing and Discount Calculation
These areas together form the complete shopping workflow.
## Expected Outcome
The expected outcome is a working Python console application that can:
•	Display grocery products and prices.
•	Track available stock.
•	Accept customer selections.
•	Maintain the shopping cart.
•	Prevent purchases beyond available stock.
•	Remove selected cart items.
•	Calculate the total bill.
•	Apply the specified discount.
•	Display the final bill clearly.


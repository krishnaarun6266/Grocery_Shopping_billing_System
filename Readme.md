# Grocery Shopping Billing System
## Project title
Grocery Shopping Billing System
## Project Overview
The program maintains a list of grocery products with their prices and available stock. A user can enter their name and mobile number, select products, enter quantities, view the cart, remove items from the cart, and complete the purchase. The program calculates the amount for each selected product and generates a final bill.
The project is implemented using core Python concepts such as dictionaries, loops, conditional statements, functions, user input, exception handling, and basic calculations.
##3. Problem Statement
In a grocery shopping environment, customers need to select required products, check available quantities, calculate the cost of their purchases, and receive a final bill. Performing these calculations manually can be time-consuming and may lead to calculation errors.
This project provides a simple Python-based solution that manages product prices and stock, allows customers to create a shopping cart, calculates item-wise costs, and generates the final payable amount.
## Objectives
•	To create a simple grocery shopping and billing system using Python.
•	To maintain product prices and available stock.
•	To allow users to select products and quantities.
•	To provide cart viewing and item removal functionality.
•	To calculate item-wise and total purchase amounts.
•	To provide a discount when the purchase amount reaches the defined threshold.
•	To apply Python Essential concepts in a practical problem.
## Functional Requirements
The system provides the following major functional modules:
### Product and Stock Management
•	Stores grocery product names and prices.
•	Stores available stock quantities.
•	Displays available products and their prices.
•	Updates stock when a product is added to the cart.
•	Restores stock when an item is removed from the cart.
### Shopping Cart Management
•	Allows the user to select a product.
•	Allows the user to enter the required quantity.
•	Adds selected products to the cart.
•	Displays the current cart.
•	Removes selected items from the cart.
•	Calculates the amount for each cart item.
### Billing and Discount
•	Calculates the amount using quantity × product price.
•	Calculates the final total of the cart.
•	Applies a 10% discount when the grand total is ₹5000 or more.
•	Displays the final payable amount.
## Input and Output Structure
### Inputs
The program accepts:
•	Customer name
•	Customer mobile number
•	Product name
•	Product quantity
•	Cart commands such as done, remove, and view
### Outputs
The program displays:
•	Product names and prices
•	Available stock
•	Cart contents
•	Item-wise amounts
•	Remaining stock
•	Total bill amount
•	Discount information, when applicable
•	Final payable amount

 
## Non-Functional Requirements
### Usability
The program uses simple text-based input and clear messages so that a user can understand the available operations.
### Reliability
The program checks whether the requested product exists and whether the requested quantity is available in stock.
### Error Handling
The program handles invalid quantity input using try-except and checks that the entered quantity is greater than zero.
### Maintainability
Product information is stored in dictionaries and the cart calculation is separated into the view_cart() function, making the code easier to modify.
### Resource Efficiency
The project uses basic Python data structures and does not require external libraries or database resources.
## Technologies and Tools Used
•	Programming Language: Python
•	Concepts Used: Variables, input/output, dictionaries, loops, conditional statements, functions, exception handling, arithmetic operations
•	Development Environment: Any Python-supported IDE or interpreter
•	Version Control: Git/GitHub
## Python Concepts Used
The project demonstrates the following Python Essential concepts:
•	Variables
•	input() and print()
•	Dictionaries
•	Dictionary methods such as .items(), .get(), and .pop()
•	if-else statements
•	while loops
•	for loops
•	Functions
•	return
•	break and continue
•	try-except
•	String methods such as .lower()
•	Arithmetic calculations
•	Comparison operators
•	Basic validation
## Installation and Run Instructions
Step 1: Install Python
Install Python 3.x on your computer if it is not already installed.
Step 2: Download or Clone the Repository
Download the project files or clone the GitHub repository.
Step 3: Open the Project
Open main.py in a Python-supported IDE such as VS Code, IDLE, PyCharm, or another Python editor.
Step 4: Run the Program
Run:
python main.py
No external Python package is required for this program.
## Testing Approach
The following test cases can be used to verify the program:
Test Case	Input/Action	Expected Result
TC01	Enter a valid product name	Product is accepted
TC02	Enter an invalid product name	Product unavailable message
TC03	Enter quantity 0	Quantity rejected
TC04	Enter a negative quantity	Quantity rejected
TC05	Enter text instead of quantity	Validation error shown
TC06	Request quantity greater than stock	Insufficient stock message
TC07	Enter view	Current cart is displayed
TC08	Enter remove and an existing cart item	Item is removed and stock is restored
TC09	Enter remove for an item not in cart	Appropriate error message
TC10	Enter done	Final bill is generated
TC11	Total below ₹5000	No 10% discount
TC12	Total ₹5000 or above	10% discount is applied
## Project Structure
Grocery-Shopping-Billing-System/

1. main.py
2. README.md
3. statement.md

The current implementation is provided in main.py. The README and statement files provide the project documentation required for the GitHub repository.
## Design and Documentation
The project documentation covers:
•	Problem Statement
•	Objectives
•	Functional Requirements
•	Non-Functional Requirements
•	System Workflow
•	Input and Output Structure
•	Technologies Used
•	Testing Approach
•	Project Structure
For the complete project report, additional design artefacts required by the course guidelines should be included where applicable.
## Implementation Details
The program uses dictionaries to maintain product prices and stock. A separate dictionary named cart stores the products selected by the customer.
The view_cart() function calculates and displays the current cart total. During shopping, the program validates product names and quantities, updates stock, and supports viewing or removing cart items.
At checkout, the program calculates the grand total and applies a 10% discount if the total is ₹5000 or more.
## Limitations of the Current Implementation
•	The program is command-line based.
•	Product and stock information are defined directly in the Python code.
•	The current version does not use a database.
•	The current version does not include a graphical user interface.
•	The current repository contains the implementation in a single Python source file.
## Conclusion
The Grocery Shopping Billing System demonstrates how Python Essential concepts can be combined to solve a practical grocery shopping and billing problem. It provides product selection, stock checking, cart management, bill calculation, and discount handling through a simple command-line interface.


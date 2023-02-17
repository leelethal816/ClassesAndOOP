import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0

customer_id = 570
name = "Danni Sellyar"
address = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
status = False

"""
customer_id = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
status = True
"""

customer = fc.Customer(customer_id, name, address, email, phone, status)

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for each in dict:
    transaction = fc.Transaction(
        dict[each][0], dict[each][1], dict[each][2], dict[each][3]
    )
    if transaction.get_customer_id() == customer.get_id():
        print(
            f"Order Item: {transaction.get_item_name()}  Price: ${transaction.get_cost():,.2f}"
        )
        order_total += transaction.get_cost()

if customer.get_status() == True:
    print(f"Total Cost: ${order_total:,.2f}")
    print(f"Member Discount: ${(order_total * 0.2):,.2f}")
    print(f"Total Cost after discount: ${(order_total * 0.8):,.2f}")
else:
    print(f"Total Cost: ${order_total:,.2f}")

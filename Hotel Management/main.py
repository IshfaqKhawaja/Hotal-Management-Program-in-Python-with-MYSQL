from prettytable import PrettyTable
from addcustomer import addcustomer
from addreservation import addreservation
from addroom import addroom
from customers import customers
from deletecustomer import deletecustomer
from deleteroom import deleteroom
from edit import edit_customer, edit_room
from reservationstatus import reservationstatus
from rooms import rooms

from rich.console import Console
from rich.markdown import Markdown
functions_list = [addcustomer, addreservation, addroom, customers, deletecustomer, deleteroom,
                  edit_customer, edit_room, reservationstatus, rooms]
view_list = ['ADD GUEST ', 'ADD RESERVATION', 'ADD ROOM', 'GUEST STATUS', 'DELETE GUEST', 'DELETE ROOM',
             'EDIT GUEST', 'EDIT ROOM', 'RESERVATION STATUS', 'ROOM STATUS']
console = Console()
with open("README.md") as readme:
    markdown = Markdown(readme.read())
console.print(markdown)

## MAIN FILE STARTS FROM HERE##
table = PrettyTable()
j = 1
table.field_names = [' PRESS   ', " FOR "]
# table.add_row([f"   0  ", f" KEY TO EXIT "])
for i in view_list:
    table.add_row([f"  {j} ", f" {i} "])
    table.add_row(['-'*25, '-'*25])
    j += 1


while True:
    print(table)
    try:
        choice = int(input("\n\tENTER YOUR CHOICE! : "))
    except Exception:
        continue
    print("\n")
    print("*"*60)
    try:
        functions_list[choice-1]()
        print("*"*60)
        print("\n")

        print("\n\t Press 'C' to continue! Any other key to Exit")
        print("-"*60)

        if input("\t").upper() == 'C':
            continue
        else:
            break
        print("\n\n")
    except IndexError:
        continue

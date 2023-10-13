import csv
from rich.console import Console
from rich.table import Table

from schemas.products import  get_products, create_products, get_product, update_product, delete_product
from schemas.suppliers import get_suppliers, create_suppliers, get_supplier, update_supplier, delete_supplier
from schemas.inventory import get_inventory_list, create_inventory, get_inventory, update_inventory, delete_inventory


def get_table(path, records):
    with open(path, "r") as file:
        reader = csv.DictReader(file)

        table = Table()

        for idx, item in enumerate(reader.fieldnames):
            table.add_column(item.upper().replace("_", " "), style=COLORS[idx])

        for item in records:
            table.add_row(*item.values())
            
        console = Console()
        console.print(table)


def interface(filename, functions):
    columns = ["Serial No.", "Option"]
    rows = functions.keys()
    path = f"/home/dev/workspace/projects/inventory-management-system/db/{filename}.csv"

    table = Table(title=filename)

    for idx, item in enumerate(columns):
        table.add_column(item, style=COLORS[idx])

    for num, option in enumerate(rows, 1):
        table.add_row(str(num), option)

    console = Console()
    console.print(table)
    
    user_input = input("Enter a serial number from above table :")

    match user_input:
        case "1":
            records = functions.get("get_list")()
            get_table(path, records)

        case "2":
            fields = {}

            for fieldname in records[0].keys():
                fields[fieldname] = input(f"Enter {fieldname}")
            functions.get("create")(**fields)
            records = functions.get("get_list")()
            get_table(path, records)
        
        case "3":
            id = input("Enter ID :")

            with open(path,"r") as file:     
                table = Table()
                
                reader = csv.DictReader(file)

                for idx, item in enumerate(reader.fieldnames):
                    table.add_column(item, style=COLORS[idx])

                item = functions.get("get_single")(id)
                table.add_row(*item.values())
                console = Console()
                console.print(table)

        case "4":
            fields = {}

            for fieldname in records[0].keys():
                fields[fieldname] = input(f"Enter {fieldname}")
            functions.get("update")(**fields)
            records = functions.get("get_list")()
            get_table(path, records)

        case "5":
            id = input("Enter ID :")
            functions.get("delete")(id)
            records = functions.get("get_list")()
            get_table(path, records)
            
        case _:
            print("Invalid Serial No.")


COLUMNS = ["Serial No.", "Option"]
ROWS = ["Inventory", "Product", "Supplier"]
COLORS = ["blue", "yellow", "cyan", "red", "green", "purple", "magenta"]

option_table = Table()

for idx, item in enumerate(COLUMNS):
    option_table.add_column(item, style=COLORS[idx])

for num, option in enumerate(ROWS, 1):
    option_table.add_row(str(num), option)

console = Console()
console.print(option_table)

user_input = input("Enter a serial number from above table :")


match user_input:
    case "1":
        functions = { 
            "get_list": get_inventory_list,
            "create": create_inventory,
            "get_single": get_inventory,
            "update": update_inventory,
            "delete": delete_inventory,
        }
        interface("inventory", functions)

    case "2":
        functions = { 
            "get_list": get_products,
            "create": create_products,
            "get_single": get_product,
            "update": update_product,
            "delete": delete_product,
        }
        interface("products", functions)

    case "3":
        functions = { 
            "get_list": get_suppliers,
            "create": create_suppliers,
            "get_single": get_supplier,
            "update": update_supplier,
            "delete": delete_supplier,
        }
        interface("suppliers", functions)

    case _:
        print("Invalid Serial No.")

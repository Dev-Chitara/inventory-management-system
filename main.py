from schemas.products import create_products, get_product, get_products, update_product, delete_product


# create_products(Product,"Apple", "Apple is very delicious", 20, 4)
# create_products(Product,"Mango", "Mango is very delicious", 25, 2)
# create_products(Product,"Banana", "Banana is very delicious", 30, 4)
# create_products(Product,"Grapes", "Grapes is very delicious", 40, 20)
# create_products(Product,"Watermelon", "Watermelon is very delicious", 35, 1)
# create_products("Strawberry", "Strawberry is very delicious", 30, 10)

# print(get_product("eb5c8796-614b-4557-a7db-9f284396322a"))

# update_product("eb5c8796-614b-4557-a7db-9f284396322a","Green apple", "Apple is very delicious", 20, 4)

# print(get_products())

print(delete_product("eb5c8796-614b-4557-a7db-9f284396322a"))


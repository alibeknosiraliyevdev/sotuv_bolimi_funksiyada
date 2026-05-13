from .database import default_database_info, finance_info, add_product_database_info
from .history_section import add_action, see_history

# log decarator
from .decarators import log_decarator

default_database = default_database_info()
add_product_database = add_product_database_info()
finance = finance_info()




@log_decarator
def add_product(product_family, product_name, quantity, buy_price, sell_price, unit):
    # Agar product family bo'lmasa
    if product_family not in default_database.keys():
        default_database[product_family] = {
            product_name: {
                "quantity": quantity,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "sold": 0,
                "unit": unit
            }
        }
        
        
        add_product_database[product_family] = {
            product_name: {
                "quantity": quantity,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "unit": unit
            }
        }
        
        finance["income"] += quantity * buy_price
        
        add_action("buy", product_name, quantity, buy_price)
        
    # Agar product family mavjud bo'lib name mavjud bo'lmasa
    elif product_name not in default_database[product_family].keys():
        default_database[product_family][product_name] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "sold": 0,
            "unit": unit
        }
        
        add_product_database[product_family][product_name] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "unit": unit
        }
        
        finance["income"] += quantity * buy_price
        add_action("buy", product_name, quantity, buy_price)
    # Agar product family va name mavjud bo'lsa
    else:
        default_database[product_family][product_name]["quantity"] += quantity
        
        add_product_database[product_family][product_name]["quantity"] += quantity
        
        finance["income"] += quantity * buy_price
        add_action("buy", product_name, quantity, buy_price)
    
        

# add_product("Drinks", "Kola", 100, 9000, 12000, "piece")

# print('\n\nQo\'shimcha ma\'lumotlar:\n\n')

# print(default_database, "\n\n\n\n")
# print(add_product_database)
# print(finance)
# print(see_history())
       
    


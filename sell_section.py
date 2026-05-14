from .database import default_database_info, finance_info, sell_product_database_info
from .history_section import add_action, see_history

# log decarator
from .decarators import log_decarator

default_database = default_database_info()
sell_product_database = sell_product_database_info()
finance = finance_info()


@log_decarator
def sell_product(product_family, product_name, quantity, sell_price,unit):
    # Agar product family bo'lmasa
    if product_family not in default_database.keys():
        print("Bunday oilasi yo'q!")
        return False
    # Agar product family mavjud bo'lib name mavjud bo'lmasa
    if product_name not in default_database[product_family].keys():
        print("Bunday mahsulot yo'q!")
        return False
    # Agar product family va name mavjud bo'lsa
    mahsulotimiz_miqdori = default_database[product_family][product_name]["quantity"]
    if mahsulotimiz_miqdori < quantity:
        print(f"Yetarli mahsulot yo'q! Omborda: {mahsulotimiz_miqdori} {unit}")
        return False
    
    default_database[product_family][product_name]["quantity"] -= quantity
    sell_product_database[product_family][product_name]["sell_price"] = sell_price
    sell_product_database[product_family][product_name]["quantity"] += quantity
        
    finance["income"] += quantity * sell_price
    add_action("sell", product_name, quantity, sell_price)
    return True
        

# add_product("Drinks", "Kola", 100, 9000, 12000, "piece")

# print('\n\nQo\'shimcha ma\'lumotlar:\n\n')

# print(default_database, "\n\n\n\n")
# print(add_product_database)
# print(finance)
# print(see_history())
       
    


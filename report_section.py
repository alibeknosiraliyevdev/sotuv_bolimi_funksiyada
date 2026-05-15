from .database import default_database_info, finance_info, add_product_database_info, sell_product_database_info
from .history_section import see_history

database_info=default_database_info() #malumotlar ko'rish
add_product=add_product_database_info() #qo'shilgan mahsulotlar
sell_product=sell_product_database_info()
history=see_history() # bajarilgan ammalar tarixi
finance = finance_info()

def admin_panel(menu):
    match menu:
        case 1:
            print(add_product)
        case 2:
            print(sell_product)
        case 3:
            print(finance)
        case 4:
            print(database_info)
        case 5:
            print(history)
    
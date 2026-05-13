from .database import default_database_info, finance_info, add_product_database_info
from .history_section import add_action, see_history

database_info=default_database_info() #malumotlar ko'rish
add_product=add_product_database_info() #qo'shilgan mahsulotlar
history=see_history() # bajarilgan ammalar tarixi
def admin_panel(son):
    if son == 3:
        print (history)
    
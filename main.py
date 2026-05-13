from .buy_section import add_product
from .report_section import admin_panel
# add_product_kiritish=add_product()
print("Sotuv bo'limizga xush kelibsiz!" .center(135))
while True:
    print("1. Mahsulot qo'shish\n2. Mahsulot sotish\n3. Admin panel\n0. Dastur yopish")
    menu=int(input("Tanlash: "))
###################################################### Add bo'limi kiritish #############################################
    if menu == 1:
        # product_family, product_name, quantity, buy_price, sell_price, unit
        add_product_kiritish=input("Oilasi , nomi, miqdori, olingan narxi, sotiladigan narxi, birligi:\n")
        if add_product_kiritish=='0':
            continue
        product_family, product_name, quantity, buy_price, sell_price, unit = add_product_kiritish.split(",")
        add_product(
            product_family.strip(),
            product_name.strip(),
            int(quantity),
            float(buy_price),
            float(sell_price),
            unit.strip()
        )
        print("Mahsulot qo'shildi!")
###################################################### Sell bo'limi kiritish #########################################





###################################################### Admin bo'limi #################################################
    elif menu == 3:
        admin_panel(3)
###################################################### Dastur yopish ##################################################
    elif menu == 0:
        break

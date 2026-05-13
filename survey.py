from .report_section import admin_panel

def choose_number(number):
    if number == 1:
        return "Mahsulot qo'shish"
    if number == 2:
        return "Mahsulot sotish"
    if number == 3:
        return admin_panel(number)
    else:
        return "Noto'g'ri amal!"
  
son=int(input("n="))
print(choose_number(son))
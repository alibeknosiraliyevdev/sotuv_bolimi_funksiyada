from .database import history_info

history = history_info()
def add_action(type, product, quantity, price):
    history.append({
        "type": type,
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": quantity * price
    })
    
def see_history():
    return history

   
    
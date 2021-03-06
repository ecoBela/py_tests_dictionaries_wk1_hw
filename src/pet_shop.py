# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] += number

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    no_of_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            no_of_pets.append(pet)
    return no_of_pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)
            
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append("new_pet")

def get_customer_cash(customers_list):
    return customers_list["cash"]

def remove_customer_cash(customers_list, cash_amount):
    customers_list["cash"] -= cash_amount

def get_customer_pet_count(customers_list):
    return len(customers_list["pets"])

def add_pet_to_customer(customers_list, new_pet):
    customers_list["pets"].append(new_pet)

def customer_can_afford_pet(customers_list, new_pet):
    if customers_list["cash"] >= new_pet["price"]:
        return True

# def customer_cannot_afford_pet(customers_list, new_pet):
#     if customers_list["cash"] < new_pet["price"]:
#         return False
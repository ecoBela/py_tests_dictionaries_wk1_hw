# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dictionary):
    return dictionary["name"]

def get_total_cash(dictionary):
    return dictionary["admin"]["total_cash"]

def add_or_remove_cash(dictionary, number):
    dictionary["admin"]["total_cash"] += number

def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

def increase_pets_sold(dictionary, number):
    dictionary["admin"]["pets_sold"] += number

def get_stock_count(dictionary):
    return len(dictionary["pets"])

def get_pets_by_breed(dictionary, breed):
    no_of_pets = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed:
            no_of_pets.append(pet)
    return no_of_pets

def find_pet_by_name(dictionary, name):
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(dictionary, name):
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            dictionary["pets"].remove(pet)
            
            
# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dictionary):
    return dictionary["name"]

def get_total_cash(dictionary):
    return dictionary["admin"]["total_cash"]

def add_or_remove_cash(dictionary, number):
    dictionary["admin"]["total_cash"] += number

def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

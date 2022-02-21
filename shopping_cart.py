# shopping_cart.py

from itertools import product
from urllib import response
import datetime
import os
from xmlrpc.client import ResponseError
from dotenv import load_dotenv
import pandas as pd


#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
products_csv = pd.read_csv(csv_filepath, header=0).to_dict('records')

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output
response = ""
product_ids = []
subtotal = 0
tax = 0
now = datetime.datetime.now()
response_validation = False
ids = []

load_dotenv() #> loads contents of the .env file into the script's environment
tax_rate = float(os.getenv("TAX_RATE")) # reads the variable from the environment

for p in products_csv:
    ids.append(p["id"])  

print("Please input product identifiers for all products in the shopping cart. Input 'DONE' when there are no items left.")  

while (response.upper() != "DONE"):
    response = input("Please input a product identifier: ")
    if (response.upper() != "DONE"):
        for i in ids:
            if int(response) == i:
                response_validation = True
        while response_validation == False:
            print("Hey, are you sure that product identifier is correct? Please try again!")
            response = input("Please input a product identifier: ")
            for i in ids:
                if int(response) == i:
                    response_validation = True
    if response.upper() != "DONE":
        product_ids.append(response)
    response_validation = False

for i in range(0, len(product_ids)):
    product_ids[i] = int(product_ids[i])


print("#> ---------------------------------")
print("#> GREEN FOODS GROCERY")
print("#> WWW.GREEN-FOODS-GROCERY.COM")
print("#> ---------------------------------")

print("#> CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M %p"))
print("#> ---------------------------------")
print("#> SELECTED PRODUCTS:")

for i in range(0, len(product_ids)):
    #for p in products:
    for p in products_csv:
        if p["id"] == product_ids[i]:
            print("#>  ... " + p["name"] + " (" + str(to_usd(p["price"])) + ")")
            subtotal = subtotal + p["price"]

tax = subtotal * tax_rate
total = subtotal + tax

#> ---------------------------------
print("#> SUBTOTAL: " + str(to_usd(subtotal)))
print("#> TAX: " + str(to_usd(tax)))
print("#> TOTAL: " + str(to_usd(total)))
print("#> ---------------------------------")
print("#> THANKS, SEE YOU AGAIN SOON!")
print("#> ---------------------------------")


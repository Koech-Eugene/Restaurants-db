import sqlite3
from models.Restaurant import Restaurant
from models.Customer import Customer
from models.Review import Review

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Connect to the database
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Test Review methods
cur.execute("SELECT * FROM reviews LIMIT 1")
review_data = cur.fetchone()
if review_data:
    review = Review(*review_data)
    customer_instance = review.customer()
    restaurant_instance = review.restaurant()
    if customer_instance:
        print("Review customer:", customer_instance.name()) 
    else:
        print("Review customer: None")
    if restaurant_instance:
        print("Review restaurant:", restaurant_instance)  
    else:
        print("Review restaurant: None")
    print("Review full review:", review.full_review())  
else:
    print("No reviews found.")

# Test Restaurant methods
cur.execute("SELECT * FROM restaurants LIMIT 1")
restaurant_data = cur.fetchone()
if restaurant_data:
    restaurant = Restaurant(*restaurant_data)
    print("Restaurant reviews:", restaurant.reviews()) 
    print("Restaurant customers:", restaurant.customers())
else:
    print("No restaurants found.")

# Test Customer methods
cur.execute("SELECT * FROM customers LIMIT 1")
customer_data = cur.fetchone()
if customer_data:
    customer = Customer(*customer_data)
    print("Customer reviews:", customer.reviews())  
    print("Customer restaurants:", customer.restaurants()) 
    print("Customer full name:", customer.name()) 
    print("Customer favorite restaurant:", customer.favorite_restaurant())  
else:
    print("No customers found.")


conn.close()

"""Test cases not well handled, missing the customers review name, fanciest restaurant
   stilll trying to figure out
"""
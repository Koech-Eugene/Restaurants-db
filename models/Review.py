"""
- `Review customer()`

 - should return the `Customer` instance for this review

- `Review restaurant()`

 - should return the `Restaurant` instance for this review
"""

import sqlite3

class Review:
    def __init__(self, id,star_rating, restaurant_id, customer_id):
        self.id = id
        self.star_rating = star_rating
        self.restaurant_id = restaurant_id  
        self.customer_id = customer_id

    def connect_database(self):
        return sqlite3.connect("database.db")
    
    def customer(self):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = ?", (self.customer_id,))
        customer_info = cur.fetchone()  
        conn.close()
        return customer_info
    
    def restaurant(self):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM restaurants WHERE id = ?", (self.restaurant_id,))
        restaurant_info = cur.fetchone()  
        conn.close()
        return restaurant_info
    
    def full_review(self):

        conn = self.connect_database()
        cur = conn.cursor()

        cur.execute("SELECT name FROM restaurants WHERE id = ?", (self.restaurant_id,))
        restaurant_name = cur.fetchone()[0]

        cur.execute("SELECT first_name, last_name FROM customers WHERE id = ?", (self.customer_id,))
        customer_info = cur.fetchone()
        
        if customer_info is not None:
            customer_name = " ".join(customer_info)
        else:
            customer_name = "Unknown"  

        conn.close()


        return f"Review for {restaurant_name} by {customer_name}: {self.star_rating} stars."

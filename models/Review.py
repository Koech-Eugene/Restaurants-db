"""
- `Review customer()`

 - should return the `Customer` instance for this review

- `Review restaurant()`

 - should return the `Restaurant` instance for this review
"""

import sqlite3

class Review:
    def __init__(self, star_rating, restaurant_id, customer_id):
        self.rating = star_rating
        self.res_id = restaurant_id
        self.cust_id = customer_id

    def connect_database():
        return sqlite3.connect("database.db")
    
    def customer(self):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = ?", (self.customer_id,))
        customer_info = cur.fetchone()  # Fetch one customer matching the ID
        conn.close()
        return customer_info
    
    def restaurant(self):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM restaurants WHERE id = ?", (self.restaurant_id,))
        restaurant_info = cur.fetchone()  # Fetch one restaurant matching the ID
        conn.close()
        return restaurant_info
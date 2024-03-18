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
    
    def full_review(self):
        # Connect to the database
        conn = self.connect_database()
        cur = conn.cursor()

        # Fetch restaurant name
        cur.execute("SELECT name FROM restaurants WHERE id = ?", (self.restaurant_id,))
        restaurant_name = cur.fetchone()[0]

        # Fetch customer's full name
        cur.execute("SELECT first_name, last_name FROM customers WHERE id = ?", (self.customer_id,))
        customer_info = cur.fetchone()
        customer_name = " ".join(customer_info)

        # Close the database connection
        conn.close()

        # Construct the full review string
        return f"Review for {restaurant_name} by {customer_name}: {self.star_rating} stars."
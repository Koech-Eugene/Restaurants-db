import sqlite3

from .Restaurant import Restaurant

class Customer:
    def __init__(self, id, first_name, last_name) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def connect_database(self):
        return sqlite3.connect("database.db")
    
    def reviews(self):
        conn = self.connect_database(self)
        cur = conn.cursor()
        cur.execute("SELECT * FROM reviews WHERE customer_id = ?", (self.id,))
        customer_reviews = cur.fetchall()  # Fetch all reviews left by the customer
        conn.close()
        return customer_reviews
    
    def restaurants(self):
        conn = self.connect_database(self)
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT restaurants.*
            FROM restaurants
            JOIN reviews ON restaurants.id = reviews.restaurant_id
            WHERE reviews.customer_id = ?
            """, (self.id,))
        reviewed_restaurants = cur.fetchall()  # Fetch all restaurants reviewed by the customer
        conn.close()
        return reviewed_restaurants

    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        conn = self.connect_database(self)
        cur = conn.cursor()
        cur.execute("""
            SELECT restaurants.*
            FROM restaurants
            JOIN reviews ON restaurants.id = reviews.restaurant_id
            WHERE reviews.customer_id = ?
            ORDER BY reviews.star_rating DESC
            LIMIT 1
            """, (self.id,))
        favorite_restaurant_info = cur.fetchone()
        conn.close()
        if favorite_restaurant_info:
            return Restaurant(*favorite_restaurant_info)
        else:
            return None
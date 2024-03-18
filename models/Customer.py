import sqlite3

class Customer:
    def __init__(self, id, first_name, last_name) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def connect_database():
        return sqlite3.connect("database.db")
    
    def reviews(self):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM reviews WHERE customer_id = ?", (self.id,))
        customer_reviews = cur.fetchall()  # Fetch all reviews left by the customer
        conn.close()
        return customer_reviews
    
    def restaurants(self):
        conn = self.connect_database()
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

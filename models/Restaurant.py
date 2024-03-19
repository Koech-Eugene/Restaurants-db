import sqlite3

class Restaurant:
    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def connect_database(self):
        return sqlite3.connect("database.db")
    
    def reviews(self):
        conn = self.connect_database(self)
        cur = conn.cursor()
        cur.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (self.id,))
        return cur.fetchall()
    
    def customers(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT customers.id, customers.first_name, customers.last_name
            FROM customers 
            JOIN reviews ON customers.id = reviews.customer_id 
            WHERE reviews.restaurant_id = ?
            """, (self.id,))
        customer_info = cur.fetchall()
        conn.close()
        return customer_info

    @classmethod
    def fanciest(cls):
        conn = cls.connect_database(cls)
        cur = conn.cursor()
        cur.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        fanciest_restaurant_info = cur.fetchone()
        conn.close()
        if fanciest_restaurant_info:
            return cls(*fanciest_restaurant_info)
        else:
            return None

    def all_reviews(self):
        conn = self.connect_database(self)
        cur = conn.cursor()
        cur.execute("""
            SELECT reviews.star_rating, customers.first_name, customers.last_name
            FROM reviews
            JOIN customers ON reviews.customer_id = customers.id
            WHERE reviews.restaurant_id = ?
            """, (self.id,))
        reviews = cur.fetchall()
        conn.close()
        formatted_reviews = [
            f"Review for {self.name} by {first_name} {last_name}: {star_rating} stars."
            for star_rating, first_name, last_name in reviews
        ]
        return formatted_reviews
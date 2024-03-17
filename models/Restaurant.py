import sqlite3

class Restaurant:
    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def connect_database():
        return sqlite3.connect("database.db")
    
    def reviews(self):
        conn = self.connect_database()
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

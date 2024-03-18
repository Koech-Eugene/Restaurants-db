import sqlite3

# have a func to create the tables
def create_tables():
    # connect to the database
    conn = sqlite3.connect("database.db")
    # create a cursor element
    cur = conn.cursor()

    # Restaurants table
    cur.execute(""" CREATE TABLE IF NOT EXISTS restaurants(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
    );

                """)

    # customers table
    cur.execute(""" CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
    );

                """)
    
    # reviews table
    cur.execute("""CREATE TABLE IF NOT EXISTS reviews(
                    review_id INTEGER PRIMARY KEY,
                    restaurant_id INTEGER,
                    customer_id INTEGER,
                    star_rating INTEGER NOT NULL,
                    FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
                    FOREIGN KEY(customer_id) REFERENCES customers(id)
                );""")

    
    # commit the changes andd close the database connection
    conn.commit()
    conn.close()

def sample_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Clear existing data
    cursor.executescript("""
    DELETE FROM Reviews;
    DELETE FROM Customers;
    DELETE FROM Restaurants;
    """)

    # Insert sample Restaurants
    restaurants = [
        ('Kwa Mathe', 'High'),  # Price here is 'Low', 'Medium', 'High'
        ('Kibandaski', 'Medium'),
        ('Chafua', 'Low'),
    ]
    cursor.executemany('INSERT INTO Restaurants (name, price) VALUES (?, ?)', restaurants)

    # Insert sample Customers
    customers = [
        ('John', 'Doe'),
        ('Jane', 'Doe'),
        ('Eugene', 'Doe'),
    ]
    cursor.executemany('INSERT INTO Customers (first_name, last_name) VALUES (?, ?)', customers)

   
    conn.commit()

    
    reviews = [
        (1, 1, 5),  
        (1, 2, 4),  
        (2, 3, 3), 
    ]
    cursor.executemany('INSERT INTO Reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)', reviews)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()
    sample_data()
    print("Database and tables createted.")
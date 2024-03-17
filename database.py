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

if __name__ == '__main__':
    create_tables()
    print("Database and tables createted.")
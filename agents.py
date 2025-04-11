from database import get_db

class CustomerAgent:
    def __init__(self, user_id):
        self.user_id = user_id

    def view_product(self, product_id):
        conn = get_db()
        conn.execute("INSERT INTO interactions (user_id, product_id, action) VALUES (?, ?, ?)",
                     (self.user_id, product_id, 'view'))
        conn.commit()
        conn.close()

class ProductAgent:
    def __init__(self, product_id):
        self.product_id = product_id

    def get_details(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = ?", (self.product_id,))
        product = cur.fetchone()
        conn.close()
        return product

from database import get_db

def recommend_products(user_id, top_n=2):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_id, COUNT(*) as views
        FROM interactions
        WHERE user_id = ?
        GROUP BY product_id
        ORDER BY views DESC
        LIMIT ?
    """, (user_id, top_n))
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

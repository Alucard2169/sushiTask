from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime


app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="sushi_user",
    password="sushipass",
    database="sushi_shop",
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci"
)

def calculate_discounts(sushi_a_count,sushi_b_count, order_time):
    total_pieces = sushi_a_count + sushi_b_count
    total_price = sushi_a_count * 3 + sushi_b_count * 4
    discount = 0
    
    
    # discount for 10 pieces
    if total_pieces >= 10:
        discount = max(discount,0.1)
    
    # discount for 20 pieces
    if total_pieces >= 20:
        discount = max(discount,0.2)
        
    # Discount during lunch time
    if order_time.hour >= 11 and order_time.hour < 14:
        discount += 0.2
    
    discounted_price = total_price * (1 - discount)
    return discounted_price, discount * 100



@app.route('/')
def home():
    return render_template('customer.html')

@app.route('/susan')
def susan():
    return render_template('owner.html')


@app.route("/api/add-to-cart", methods=['POST'])
def add_to_cart():
    data = request.json
    sushi_a_count = data.get("sushi_a_count")
    sushi_b_count = data.get("sushi_b_count")
    order_time = datetime.now()
    
    total_price, discount = calculate_discounts(sushi_a_count, sushi_b_count, order_time)
    
    cursor = db.cursor()
    
    sql = """INSERT INTO sushi_orders 
             (sushi_a_count, sushi_b_count, total_price, discount_applied, order_time) 
             VALUES (%s, %s, %s, %s, %s)"""
    values = (sushi_a_count, sushi_b_count, total_price, discount, order_time)
    cursor.execute(sql, values)
    db.commit()
    
    return jsonify({
        "success":True,
        "total_price":total_price,
        "discount":discount
    })


@app.route("/api/orders", methods=['GET'])
def get_orders():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sushi_orders ORDER BY order_time DESC")
    orders = cursor.fetchall()
    print("")
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"id": 1, "user_id": 101, "status": "Shipped"},
    {"id": 2, "user_id": 101, "status": "Processing"},
    {"id": 3, "user_id": 102, "status": "Delivered"}
]

# Get orders by user
@app.route("/orders/user/<int:user_id>")
def get_orders(user_id):
    user_orders = [o for o in orders if o["user_id"] == user_id]
    return jsonify(user_orders)

# Update order status
@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()

    for order in orders:
        if order["id"] == order_id:
            order["status"] = data.get("status", order["status"])
            return jsonify(order)

    return jsonify({"error": "Order not found"}), 404

@app.route("/")
def home():
    return jsonify({"service": "Order Service Running"})

if __name__ == "__main__":
    app.run(port=5002, debug=True)
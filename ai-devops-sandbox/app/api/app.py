from flask import Flask, request, jsonify
from orders import apply_bulk_discount

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/orders/quote")
def quote():
    items = request.json.get("items", [])
    total = apply_bulk_discount(items)
    return jsonify(total=total)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

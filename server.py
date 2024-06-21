from flask import Flask, request
from dotenv import load_dotenv
from groq import Groq
import json
import os
import re

# Load environment variables from .env file (e.g., API keys)
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Initialize the Groq language model interface
cached_llm = Groq(api_key=GROQ_API_KEY)

# Create a Flask app instance
app = Flask(__name__)

# Path to the database file
DB_FILE = "database/company_db.json"


def ensure_db_exists():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({}, f)


def classify_product_llm(product_name, price):
    prompt = f"""
    Classify the following product into a shipping slot based on its price:
    Product: {product_name}
    Price: ${price}

    Shipping slots:
    Slot 1: Price <= $25
    Slot 2: $25 < Price <= $50
    Slot 3: $50 < Price <= $75
    Slot 4: $75 < Price <= $100
    Slot 5: Price > $100

    Respond with only the slot number (1, 2, 3, 4, or 5).
    """
    response = cached_llm.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1024
    )
    try:
        slot = int(response.choices[0].message.content.strip())
        if 1 <= slot <= 5:
            return slot
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid LLM response: {response.choices[0].message.content}")
        return None


def extract_price(product_details):
    price_match = re.search(r'Price: \$(\d+(\.\d{1,2})?)', product_details)
    if price_match:
        return float(price_match.group(1))
    return None


@app.route("/llm", methods=["POST"])
def handle_llm():
    json_content = request.json
    print(json_content)
    product_name = json_content.get("product_name")
    product_details = json_content.get("product_details")
    print("Extract Price")
    # Extract price and classify product
    price = extract_price(product_details)
    if price is not None:
        print("call LLM")
        slot = classify_product_llm(product_name, price)
        if slot is not None:
            # Ensure the database file exists
            ensure_db_exists()

            # Read existing data
            with open(DB_FILE, 'r') as f:
                db = json.load(f)

            # Append new classification
            if product_name not in db:
                db[product_name] = []
            db[product_name].append({"price": price, "slot": slot})

            # Write updated data back to file
            with open(DB_FILE, 'w') as f:
                json.dump(db, f, indent=2)

    response = {
        "status": "success",
        "message": "Your product has been initiated for shipping.",
        "order_details": {
            "status": "processing",
            "processing ETA": "1-2 business days"
        }
    }

    return json.dumps(response, indent=2)


# Start the app
def start_app():
    # Start the Flask server on port 8080, accessible to all network interfaces.
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()

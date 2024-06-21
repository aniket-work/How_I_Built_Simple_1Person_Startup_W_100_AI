from flask import Blueprint, request, jsonify
from services.llm_service import LLMService
from models.database import Database

product_bp = Blueprint('product', __name__)

@product_bp.route("/llm", methods=["POST"])
def handle_llm():
    json_content = request.json
    product_name = json_content.get("product_name")
    product_details = json_content.get("product_details")

    slot = LLMService.classify_product(product_name, product_details)
    if slot is not None:
        Database.append_product(product_name, slot)

    response = {
        "status": "success",
        "message": "Your product has been initiated for shipping.",
        "order_details": {
            "status": "processing",
            "processing ETA": "1-2 business days"
        }
    }

    return jsonify(response)
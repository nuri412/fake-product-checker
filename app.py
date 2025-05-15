import streamlit as st
import qrcode
import hashlib
import uuid
import json
import os

# Путь к «блокчейну»
BLOCKCHAIN_FILE = "blockchain.json"

# Загружаем или создаем цепочку
if os.path.exists(BLOCKCHAIN_FILE):
    with open(BLOCKCHAIN_FILE, "r") as f:
        blockchain = json.load(f)
else:
    blockchain = []

# Создание блока
def create_block(product_id):
    previous_hash = blockchain[-1]['hash'] if blockchain else "0"
    block = {
        "product_id": product_id,
        "previous_hash": previous_hash,
    }
    block_string = json.dumps(block, sort_keys=True).encode()
    block_hash = hashlib.sha256(block_string).hexdigest()
    block["hash"] = block_hash
    blockchain.append(block)
    save_blockchain()
    return block

def save_blockchain():
    with open(BLOCKCHAIN_FILE, "w") as f:
        json.dump(blockchain, f, indent=4)

# Проверка подлинности
def verify_product(product_id):
    for block in blockchain:
        if block['product_id'] == product_id:
            return True
    return False

# Интерфейс
st.set_page_config(page_title="Fake Product Checker - Blockchain QR")
st.title("🔍 Fake Product Identification System")

menu = st.sidebar.selectbox("Choose Option", ["Register Product", "Verify Product"])

if menu == "Register Product":
    st.header("✅ Register a Genuine Product")
    product_name = st.text_input("Product Name")
    if st.button("Generate QR + Register"):
        if product_name:
            product_id = str(uuid.uuid4())
            block = create_block(product_id)
            qr = qrcode.make(product_id)
            qr_path = f"qr_{product_name.replace(' ', '_')}.png"
            qr.save(qr_path)
            st.image(qr_path, caption="Scan this QR to verify")
            st.success(f"Product Registered with ID: {product_id}")
        else:
            st.warning("Please enter a product name")

elif menu == "Verify Product":
    st.header("🔎 Verify Product Authenticity")
    qr_code = st.text_input("Paste QR Code (Product ID) here")
    if st.button("Verify"):
        if verify_product(qr_code):
            st.success("✅ This product is GENUINE and registered in blockchain.")
        else:
            st.error("❌ This product is FAKE or not registered.")

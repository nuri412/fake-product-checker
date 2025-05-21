# Fake Product Identification System 🔍

A blockchain-based solution for identifying counterfeit products using QR codes. This project implements a simple yet effective system to register and verify authentic products using blockchain principles.

## Features 

- Product registration with unique identifiers
- Automatic QR code generation for each product
- Blockchain-based verification system
- Simple web interface built with Streamlit
- Immutable record keeping using JSON-based blockchain

## Prerequisites 

- Python 3.7 or higher
- pip (Python package manager)

## Installation 

1. Clone the repository:
```bash
git clone https://github.com/nuri412/fake-product-checker
cd fake-product-checker-main
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

### Product Registration:

1. Select "Register Product" from the sidebar
2. Enter the product name
3. Click "Generate QR + Register"
4. The system will:
   - Generate a unique Product ID
   - Create a blockchain entry
   - Generate and save a QR code
   - Display the QR code and Product ID

### Product Verification:

1. Select "Verify Product" from the sidebar
2. Enter the Product ID or scan the QR code
3. Click "Verify" to check authenticity
4. System will display whether the product is genuine or fake

## Project Structure 

```
fake-product-checker/
├── app.py              # Main application file
├── blockchain.json     # Blockchain storage
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── qr_*.png           # Generated QR codes
```

## Technical Details 

### Blockchain Structure

Each block in the blockchain contains:
```json
{
    "product_id": "unique-uuid",
    "previous_hash": "hash-of-previous-block",
    "hash": "current-block-hash"
}
```

### Dependencies

- `streamlit`: Web interface framework
- `qrcode`: QR code generation
- `hashlib`: Cryptographic hashing
- `uuid`: Unique identifier generation

## Security Features 

- Hash-based block linking
- Immutable record keeping
- Unique product identification
- Tamper-evident design

## Contributing 

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 

This project is licensed under the MIT License.

---
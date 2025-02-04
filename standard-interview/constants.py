"""
Constants for the sales data processing pipeline.
Currently not used in the implementation (bug?).
"""

# Currency conversion rates to USD
CURRENCY_RATES = {
    'USD': 1.0,      # Base currency
    'EUR': 1.1,      # 1 EUR = 1.1 USD
    'GBP': 1.25,     # 1 GBP = 1.25 USD
    'JPY': 0.0067    # 1 JPY = 0.0067 USD
}

# Required columns for CSV files
REQUIRED_COLUMNS = {
    'sales': ['date', 'product_sku', 'sales', 'currency', 'quantity'],
    'margins': ['product_sku', 'cost', 'margin_percentage', 'valid_from', 'valid_to']
}
"""
Module for transforming and cleaning sales data.
"""
from typing import List, Dict
from datetime import datetime

def calculate_profit(sale: Dict, margins: Dict[str, List[Dict]]) -> float:
    """
    Calculate profit for a sale using margin data.

    Args:
        sale (Dict): A dictionary representing a sale record
        margins (Dict[str, List[Dict]]): A dictionary of product margins
        
    Returns:
        float: The calculated profit for the sale
    """
    sku = sale['product_sku']
    
    if sku not in margins:
        return 0.0
    
    sale_date = sale['date']
    
    sale_datetime = datetime.strptime(sale_date, '%Y-%m-%d')
    
    margin_data = margins[sku][0]
    
    revenue = float(sale['sales'])

    cost = margin_data['cost'] * int(sale['quantity'])
    
    return revenue - cost

def find_applicable_margin(sku: str, date: str, margins: Dict) -> Dict:
    """
    Find the applicable margin for a given SKU and date.

    Raise an error for dates without valid margin
    """
    if sku not in margins:
        return None
        
    # TODO: Currently returns first margin without checking dates, should check dates
    return margins[sku][0]

def clean_data(records: List[Dict], margins: Dict) -> List[Dict]:
    """
    Clean and transform sales records with margin calculations.
    """
    cleaned_records = []
    
    for record in records:
        try:
            sku = record['product_sku']
            date = record['date']
            sales = float(record['sales'])
            quantity = int(record['quantity'])
            currency = record['currency']
            
            margin_data = find_applicable_margin(sku, date, margins)
            if margin_data:
                cost = margin_data['cost'] * quantity
                profit = sales - cost
                
                margin_percentage = margin_data['margin']  # Should calculate from profit
                
                cleaned_record = {
                    'date': date,
                    'product_sku': sku,
                    'sales_usd': sales,
                    'quantity': quantity,
                    'currency': currency,
                    'cost': cost,
                    'profit': profit,
                    'profit_margin': margin_percentage
                }
                cleaned_records.append(cleaned_record)
                
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid record: {record}")
            
    return cleaned_records

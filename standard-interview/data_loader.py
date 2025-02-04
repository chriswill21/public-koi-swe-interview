"""
Module for loading sales data from CSV files.
"""
import csv
import os
from typing import List, Dict

def load_data(directory: str) -> List[Dict]:
    """
    Load data from all CSV files in the specified directory.
    
    Args:
        directory (str): Path to directory containing CSV files
        
    Returns:
        List[Dict]: Combined list of sales records
    """
    all_records = []
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)

            first_record = next(reader)
            records = [first_record] + list(reader)

            all_records.extend(records)
    
    return all_records

def load_margins(directory: str) -> Dict[str, List[Dict]]:
    """
    Load product margins with validity periods.
    
    Args:
        directory (str): Path to directory containing product_margins.csv
        
    Returns:
        Dict[str, List[Dict]]: Dictionary of margin records by SKU
        
    """
    margins_by_sku = {}
    margins_file = os.path.join(directory, 'product_margins.csv')
    
    with open(margins_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            sku = row['product_sku']
            if sku not in margins_by_sku:
                margins_by_sku[sku] = []
            
            margin_data = {
                'cost': float(row['cost']),
                'margin': float(row['margin_percentage']),
                'valid_from': row['valid_from'],
                'valid_to': row['valid_to']
            }

            margins_by_sku[sku].append(margin_data)
    
    return margins_by_sku

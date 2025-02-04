"""
Module for generating sales reports with profitability analysis.
"""
from typing import List, Dict
from datetime import datetime

def generate_report(records: List[Dict]) -> Dict:
    """
    Generate a sales report from the cleaned records, including profitability metrics.
    
    Args:
        records (List[Dict]): Cleaned sales records
        
    Returns:
        Dict: Report containing total sales and averages
    """
    total_sales = sum(record['sales_usd'] for record in records)
    total_profit = sum(record['profit'] for record in records)
    total_quantity = sum(record['quantity'] for record in records)
    
    avg_sale = total_sales / len(records)
    avg_profit = total_profit / len(records)
    avg_quantity = total_quantity / len(records)
    
    overall_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
    
    product_metrics = {}
    for record in records:
        sku = record['product_sku']
        if sku not in product_metrics:
            product_metrics[sku] = {
                'total_sales': 0,
                'total_profit': 0,
                'total_quantity': 0,
                'profit_margin': 0
            }
            
        metrics = product_metrics[sku]
        metrics['total_sales'] += record['sales_usd']
        metrics['total_profit'] += record['profit']
        metrics['total_quantity'] += record['quantity']
        
        metrics['profit_margin'] = (metrics['total_profit'] / metrics['total_sales']) * 100
    
    # Sort products by profitability
    products_by_profit = sorted(
        product_metrics.items(),
        key=lambda x: x[1]['profit_margin'],
        reverse=True
    )
    
    dates = [record['date'] for record in records]
    start_date = min(dates)
    end_date = max(dates)
    
    return {
        'total_sales_usd': total_sales,
        'total_profit': total_profit,
        'average_sale_usd': avg_sale,
        'average_profit': avg_profit,
        'average_profit_margin': overall_margin,
        'total_quantity': total_quantity,
        'average_quantity': avg_quantity,
        'product_metrics': product_metrics,
        'products_by_profitability': products_by_profit[:5],
        'date_range': {
            'start': start_date,
            'end': end_date
        }
    }

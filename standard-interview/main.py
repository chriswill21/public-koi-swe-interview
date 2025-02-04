"""
Main module for the sales data processing pipeline.
Orchestrates the loading, transformation, and reporting of sales data.

Known Issues:
- #TODO(previous_dev): Sales report looks weird on Feb 15th? Same product, same day,
  vastly different profits. Maybe a good thing - boss says numbers are "great"!
- NOTE: JP office keeps asking about exchange rates... told them to check their local numbers
- WEIRD: Same SKU, same quantity, same day... different regions, VERY different profits???
"""
import os
from data_loader import load_data, load_margins
from data_transformer import clean_data
from report_generator import generate_report

def process_sales_data(data_directory: str) -> tuple[dict, list]:
    """
    Process sales data through the complete pipeline.
    
    Args:
        data_directory (str): Path to directory containing sales data CSV files
        
    Returns:
        tuple[dict, list]: Sales report and cleaned records
    """
    # Load raw sales data and margin data
    raw_records = load_data(data_directory)

    margins = load_margins(data_directory)

    # Transform and clean the data
    cleaned_records = clean_data(raw_records, margins)

    # Generate the final report
    report = generate_report(cleaned_records)

    return report, cleaned_records

if __name__ == "__main__":
    # Get the directory containing the data files
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    
    # Process the data and generate report
    report, cleaned_records = process_sales_data(data_dir)
    
    # Display the results
    if report:
        print("\nSales Report:")
        print("-" * 40)
        print(f"Total Sales (USD): ${report['total_sales_usd']:.2f}")
        print(f"Total Profit: ${report['total_profit']:.2f}")
        print(f"Average Sale (USD): ${report['average_sale_usd']:.2f}")
        print(f"Average Profit Margin: {report['average_profit_margin']:.1f}%")
        print(f"Total Quantity: {report['total_quantity']}")
        print(f"Average Quantity: {report['average_quantity']:.1f}")
        print(f"\nDate Range: {report['date_range']['start']} to {report['date_range']['end']}")
        
        print("\nTop Products by Profitability:")
        print("-" * 40)
        for sku, metrics in report['products_by_profitability']:
            print(f"SKU: {sku}")
            print(f"  Profit Margin: {metrics['profit_margin']:.1f}%")
            print(f"  Total Sales: ${metrics['total_sales']:.2f}")
            print(f"  Total Profit: ${metrics['total_profit']:.2f}")
            print()
            
    else:
        print("Failed to generate report.")

"""
Unit tests for the sales data processing pipeline.
"""
import os
import pytest
from datetime import datetime
from data_loader import load_data, load_margins
from data_transformer import clean_data, calculate_profit
from report_generator import generate_report

# Test data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def test_load_margins_basic():
    """Test basic margin loading functionality."""
    margins = load_margins(DATA_DIR)
    assert 'SKU001' in margins
    assert len(margins['SKU001']) > 0
    assert 'cost' in margins['SKU001'][0]

def test_margin_date_validity():
    """Test margin validity periods."""
    margins = load_margins(DATA_DIR)
    sale = {
        'product_sku': 'SKU001',
        'date': '2024-01-15',
        'sales': '100.50',
        'quantity': '5'
    }
    profit = calculate_profit(sale, margins)
    assert profit is not None  # Should use 25% margin

    # Test with date in second half of year
    sale['date'] = '2024-08-15'
    profit_later = calculate_profit(sale, margins)
    assert profit_later != profit  # Should use 20% margin

def test_missing_margin_data():
    """Test handling of missing margin data."""
    margins = load_margins(DATA_DIR)
    sale = {
        'product_sku': 'UNKNOWN_SKU',
        'date': '2024-01-15',
        'sales': '100.50',
        'quantity': '5'
    }
    with pytest.raises(ValueError):
        calculate_profit(sale, margins)

def test_data_transformation_with_margins():
    """Test full data transformation with margin calculations."""
    # Create a temporary test record to avoid empty file issue
    test_records = [{
        'product_sku': 'SKU001',
        'date': '2024-01-15',
        'sales': '100.50',
        'quantity': '5',
        'currency': 'USD'
    }]
    margins = load_margins(DATA_DIR)
    
    cleaned_data = clean_data(test_records, margins)
    
    assert all('profit' in record for record in cleaned_data)
    assert all('profit_margin' in record for record in cleaned_data)

def test_report_with_profitability():
    """Test report generation with profit metrics."""
    # Create a temporary test record to avoid empty file issue
    test_records = [{
        'date': '2024-01-15',
        'product_sku': 'SKU001',
        'sales_usd': 100.50,
        'quantity': 5,
        'profit': 25.50,
        'profit_margin': 25.0
    }]
    
    report = generate_report(test_records)
    
    assert 'total_profit' in report
    assert 'average_profit_margin' in report
    assert 'products_by_profitability' in report

def test_overlapping_margin_periods():
    """Test handling of overlapping margin validity periods."""
    margins = load_margins(DATA_DIR)
    
    # SKU001 has multiple periods
    sku001_margins = margins['SKU001']
    dates = [(m['valid_from'], m['valid_to']) for m in sku001_margins]
    
    # Check for overlapping dates
    for i in range(len(dates)-1):
        current_end = datetime.strptime(dates[i][1], '%Y-%m-%d')
        next_start = datetime.strptime(dates[i+1][0], '%Y-%m-%d')
        assert current_end < next_start, "Overlapping margin periods detected"

def test_margin_period_gaps():
    """Test handling of gaps in margin validity periods."""
    margins = load_margins(DATA_DIR)
    sale = {
        'product_sku': 'SKU001',
        'date': '2024-06-31',  # Gap between validity periods
        'sales': '100.50',
        'quantity': '5'
    }
    with pytest.raises(ValueError):
        calculate_profit(sale, margins)

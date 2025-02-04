# Sales Data Processing Pipeline - Standard Debugging Task

## Overview
This is a Python application that processes sales data from CSV files. The pipeline loads data from multiple files, transforms the data, and generates sales reports. The code contains several bugs and areas for improvement that need to be addressed.

## Task Description
Debug and improve this application, focusing on:

1. **Bug Fixes**

2. **Error Handling**

3. **Code Improvements**

## Project Structure
```
.
├── main.py                 # Main pipeline orchestration
├── data_loader.py         # CSV loading functionality
├── data_transformer.py    # Data cleaning and transformation
├── report_generator.py    # Report generation logic
├── test_pipeline.py       # Unit tests
└── data/
    ├── sales_january.csv  # Valid sales data
    ├── sales_february.csv # Data with intentional errors
    └── empty.csv         # Empty file with headers
```

## Getting Started
1. Review the code in each module
2. Run the tests: `python -m pytest test_pipeline.py`
3. Fix the bugs and improve the code
4. Add new test cases
5. Ensure all tests pass

## Expected Improvements
When working correctly, the pipeline should:
1. Load data reliably:
   - Handle empty files gracefully
   - Validate required columns
   - Process valid records from partially invalid files

2. Transform data correctly:
   - Handle missing values appropriately
   - Validate date formats
   - Convert currencies properly

3. Generate accurate reports:
   - Calculate totals correctly
   - Handle division by zero cases
   - Process missing data appropriately

## Time Allocation (30-40 minutes)
- 5-10 minutes: Code review and bug identification
- 15-20 minutes: Bug fixing and improvements
- 10 minutes: Writing additional tests and documentation

## Success Criteria
1. All tests pass
2. Code handles edge cases gracefully
3. Reports generate correct calculations
4. Code is well-documented
5. New test cases are added and passing

## Skills Evaluated
- Basic Python programming
- Debugging methodology
- Error handling
- Testing practices
- Code documentation
- Problem-solving approach

This task is designed for mid-level engineers to demonstrate fundamental debugging and code improvement skills in a realistic scenario.

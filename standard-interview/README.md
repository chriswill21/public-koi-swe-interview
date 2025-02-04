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
3. Fix the bugs and improve the code to ensure the tests pass
4. Run main.py to ensure it executes
5. Examine the output from main.py to check that the outputs make sense

## Success Criteria
1. All tests pass
2. Code handles edge cases gracefully
3. Reports generate correct calculations
4. Code is well-documented

## Skills Evaluated
- Basic Python programming
- Debugging methodology
- Error handling
- Testing practices
- Code documentation
- Problem-solving approach

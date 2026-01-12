# Gematria Tool - Exploration Notes

## Project Overview
A Python tool for calculating gematria (Hebrew) and isopsephy (Greek) numeric values from text input.

## What is Gematria/Isopsephy?

### Gematria (Hebrew)
- Assigns numeric values to Hebrew letters
- Common systems:
  - **Absolute Value (Mispar Hechrechi)**: א=1, ב=2, ג=3, ..., י=10, כ=20, ..., ק=100, ר=200, ש=300, ת=400
  - **Ordinal Value (Mispar Siduri)**: א=1, ב=2, ג=3, ..., ת=22
  - **Reduced Value (Mispar Katan)**: Sum digits until single digit (e.g., 26 → 2+6=8)
  - **Mispar Gadol**: Similar to absolute but includes final forms (ך=500, ם=600, ן=700, ף=800, ץ=900)

### Isopsephy (Greek)
- Assigns numeric values to Greek letters
- Standard mapping: α=1, β=2, γ=3, ..., ι=10, κ=20, ..., ρ=100, σ=200, ..., ω=800

## Potential Applications in Investment Context

1. **Pattern Recognition**: Identifying numeric patterns in company names, ticker symbols
2. **Symbolic Analysis**: Exploring connections between names and values
3. **Data Analysis**: Using numeric values as features in ML models
4. **Research Tool**: For exploring historical or symbolic connections

## Implementation Plan

### Core Features
1. Hebrew gematria calculator with multiple systems
2. Greek isopsephy calculator
3. Text input validation and normalization
4. Multiple calculation methods (absolute, ordinal, reduced)
5. Batch processing capabilities
6. Export results (CSV, JSON)

### Technical Stack
- Python 3.x
- Unicode support for Hebrew/Greek characters
- Command-line interface
- Optional: Web interface, API

### Project Structure
```
gematria_tool/
├── src/
│   ├── __init__.py
│   ├── gematria.py      # Hebrew gematria calculations
│   ├── isopsephy.py     # Greek isopsephy calculations
│   └── utils.py         # Text normalization, validation
├── tests/
│   ├── test_gematria.py
│   └── test_isopsephy.py
├── examples/
│   └── example_usage.py
├── requirements.txt
├── setup.py
└── README.md
```

## Next Steps
1. Set up project structure
2. Implement Hebrew gematria calculator
3. Implement Greek isopsephy calculator
4. Add CLI interface
5. Write tests
6. Add documentation

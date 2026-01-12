# Gematria Tool

Gematria Tool is a small, dependency-free Python package and CLI for computing
numeric values (gematria/isopsephy) for Hebrew and Greek text using standard
letter-to-number mappings. It is designed for quick analysis, reproducible
results, and easy integration into research or text-processing pipelines.

## Features

- Computes Hebrew (mispar gadol) and Greek (isopsephy) values.
- CLI and Python API for easy scripting.
- Normalizes input by stripping whitespace and punctuation.
- Extensible mapping tables for custom alphabets.

## Requirements

- Python 3.10+

## Installation

```bash
pip install -e .
```

## Usage

### CLI

```bash
gematria-tool --language hebrew "בראשית"
# -> 913

gematria-tool --language greek "λογος"
# -> 373
```

### Python API

```python
from gematria_tool import gematria

value = gematria("בראשית", language="hebrew")
print(value)  # 913
```

## Testing

```bash
pytest
```

## Project Structure

- `src/gematria_tool/`: core library
- `tests/`: unit tests
- `.github/workflows/`: CI configuration

## License

MIT License.

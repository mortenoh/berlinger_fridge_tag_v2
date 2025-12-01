# Berlinger FridgeTag Parser

Parser for Berlinger Fridge-tag 2 export files using ANTLR4.

Supports both Python and JavaScript with identical JSON output.

## Quick Start

```bash
# Install dependencies and generate parsers
make install
make generate

# Test both parsers
make test
```

## Usage

### Python

```bash
# Parse file to stdout
uv run -m berlinger.fridgetag_json data/fridgetag/file.txt

# Compact output
uv run -m berlinger.fridgetag_json data/fridgetag/file.txt --compact

# Write to file
uv run -m berlinger.fridgetag_json data/fridgetag/file.txt -o output.json
```

### JavaScript

```bash
# Parse file to stdout
node src/js/fridgetag_json.js data/fridgetag/file.txt

# Compact output
node src/js/fridgetag_json.js data/fridgetag/file.txt --compact

# Write to file
node src/js/fridgetag_json.js data/fridgetag/file.txt -o output.json
```

## Project Structure

```
py_berlinger/
├── grammars/                  # ANTLR grammar files
│   └── BerlingerFridgeTagLine.g4
├── src/
│   ├── berlinger/             # Python package
│   │   ├── __init__.py
│   │   ├── keys.py            # Key constants
│   │   ├── fridgetag_parser.py
│   │   └── fridgetag_json.py  # CLI tool
│   └── js/                    # JavaScript implementation
│       ├── keys.js
│       ├── fridgetag_parser.js
│       └── fridgetag_json.js  # CLI tool
├── data/fridgetag/            # Test data files
├── generated/                 # ANTLR-generated parsers (gitignored)
├── pyproject.toml
├── package.json
└── Makefile
```

## Development

```bash
make help      # Show available commands
make lint      # Format and lint code
make clean     # Remove generated files
```

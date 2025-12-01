.PHONY: help install generate build lint check test test-all clean

GRAMMAR_DIR := grammars
GENERATED_DIR := generated

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install    Install Python and Node dependencies"
	@echo "  generate   Generate ANTLR parsers (Python + JavaScript)"
	@echo "  lint       Format and lint code"
	@echo "  check      Check code without fixing"
	@echo "  build      Parse all input files to JSON output"
	@echo "  test       Run parser on test data"
	@echo "  test-all   Run cross-implementation comparison tests"
	@echo "  clean      Remove generated files and caches"

install:
	@echo ">>> Installing Python dependencies"
	@uv sync
	@echo ">>> Installing Node dependencies"
	@npm install

generate: generate-python generate-js

generate-python:
	@echo ">>> Generating Python parser"
	@mkdir -p $(GENERATED_DIR)/BerlingerFridgeTag/grammars
	@cd $(GRAMMAR_DIR) && antlr -Dlanguage=Python3 -visitor \
		-o ../$(GENERATED_DIR)/BerlingerFridgeTag/grammars \
		BerlingerFridgeTag.g4

generate-js:
	@echo ">>> Generating JavaScript parser"
	@mkdir -p $(GENERATED_DIR)/BerlingerFridgeTag/js/grammars
	@cd $(GRAMMAR_DIR) && antlr -Dlanguage=JavaScript -visitor \
		-o ../$(GENERATED_DIR)/BerlingerFridgeTag/js/grammars \
		BerlingerFridgeTag.g4
	@echo '{"type": "module"}' > $(GENERATED_DIR)/BerlingerFridgeTag/js/package.json

lint:
	@echo ">>> Formatting and linting"
	@uv run ruff format .
	@uv run ruff check . --fix

check:
	@echo ">>> Checking code"
	@uv run ruff check .
	@uv run ruff format --check .

build:
	@echo ">>> Parsing input files to JSON"
	@mkdir -p data/output
	@for file in data/input/*.txt; do \
		name=$$(basename "$$file" .txt); \
		uv run -m berlinger.fridgetag_json "$$file" > "data/output/$$name.json"; \
		echo "  $$name.json"; \
	done

test:
	@echo ">>> Testing Python parser"
	@uv run -m berlinger.fridgetag_json data/input/160400343949_202503171012.txt --compact | head -c 200
	@echo ""
	@echo ""
	@echo ">>> Testing JavaScript parser"
	@node src/js/fridgetag_json.js data/input/160400343949_202503171012.txt --compact | head -c 200
	@echo ""

test-all:
	@echo ">>> Running cross-implementation comparison tests"
	@./tests/compare.sh

clean:
	@echo ">>> Cleaning"
	@rm -rf $(GENERATED_DIR)
	@rm -rf node_modules
	@rm -rf .ruff_cache
	@rm -rf .venv
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

.DEFAULT_GOAL := help

#!/bin/bash
# Cross-implementation comparison test
# Verifies Python and JavaScript parsers produce identical output

PASS=0
FAIL=0

echo "=== Valid files (output must match) ==="
for file in tests/fixtures/valid/*.txt; do
  py_out=$(uv run -m berlinger.fridgetag_json "$file" 2>/dev/null)
  js_out=$(node src/js/fridgetag_json.js "$file" 2>/dev/null)

  if [ "$py_out" = "$js_out" ]; then
    echo "✓ $(basename $file)"
    ((PASS++))
  else
    echo "✗ $(basename $file)"
    echo "  Python: ${py_out:0:100}..."
    echo "  JS:     ${js_out:0:100}..."
    ((FAIL++))
  fi
done

echo ""
echo "=== Invalid files (output must match) ==="
for file in tests/fixtures/invalid/*.txt; do
  py_out=$(uv run -m berlinger.fridgetag_json "$file" 2>/dev/null)
  js_out=$(node src/js/fridgetag_json.js "$file" 2>/dev/null)

  if [ "$py_out" = "$js_out" ]; then
    echo "✓ $(basename $file)"
    ((PASS++))
  else
    echo "✗ $(basename $file)"
    ((FAIL++))
  fi
done

echo ""
echo "Passed: $PASS, Failed: $FAIL"
[ $FAIL -eq 0 ]

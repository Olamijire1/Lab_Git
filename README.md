# Matrix Multiplication

## Overview

The `matrix_mul` script provides a function to multiply two matrices.

## Usage

### Running the Script

Ensure you have Python 3 installed. To run the script:

```bash
python matrix_mul.py
```

### Function: `matrix_mul`

The `matrix_mul` function multiplies two matrices.

```python
result_matrix = matrix_mul(matrix_a, matrix_b)
```

**Parameters:**
- `matrix_a` (list): The first matrix.
- `matrix_b` (list): The second matrix.

**Returns:**
- `result_matrix` (list): The resulting matrix after multiplication.

**Raises:**
- `TypeError`: If `matrix_a` or `matrix_b` is not a list or a list of lists.
- `ValueError`: If `matrix_a` or `matrix_b` is empty, if matrices cannot be multiplied, or if dimensions are invalid.

### Example

```python
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

result_matrix = matrix_mul(matrix_a, matrix_b)
print(result_matrix)
```

## Testing

The script includes a test file `matrix_mul_test.txt` using doctest. To run tests:

```bash
python matrix_mul.py
```

## Documentation

For detailed documentation and examples, refer to the docstrings in the script.

```python
"""
Multiply two matrices.

Args:
    matrix_a (list): The first matrix.
    matrix_b (list): The second matrix.

Returns:
    list: The resulting matrix after multiplication.

Raises:
    TypeError: If matrix_a or matrix_b is not a list or a list of lists.
    ValueError: If matrix_a or matrix_b is empty or if matrices cannot be multiplied.

    python3 
        TypeError: matrix_a should contain only integers or floats
"""
```

---

# Rank-Based Inverse Normal Transformation

This Python script provides a utility for applying a rank-based inverse normal transformation to a numpy array or 2-D matrix. It is designed to transform input data such that it is normally distributed, which can be particularly useful in statistical analyses where normality is assumed.

## Features

- **Inverse Normal Transformation**: Transforms data to a normal distribution using rank-based methods.
- **Handling Repeated Values**: Includes functionality to handle repeated values within the data by replacing them with the mean of those values.
- **Multiple Transformation Methods**: Supports different methods for the transformation, including Blom, Tukey, Bliss, and Van der Waerden's method.

## Requirements

- numpy
- scipy
- math

Ensure these libraries are installed in your environment to use the script successfully.

## Usage

1. Import the script into your Python environment.
2. Call the `inverse_normal` function with your data array as the argument. Optionally, specify the transformation method and whether your data contains repeated values.

```python
import numpy as np
from your_script_name import inverse_normal

# Example data
X = np.random.rand(100, 1)

# Apply the inverse normal transformation
X_trans = inverse_normal(X, method='Blom', repeat_val=False)

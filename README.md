# cheme_545_hw1
This repository contains implementations for functions that parsing a dictionary containing lab data and compute molecular weights.

For the `extract_parameter` function, I used brackets to index into the dictionaries and lists. I used a `try` `except` block to handle key errors and index errors.

Example usage:
```
from extract_parameter import extract_parameter
extract_parameter("distillation_column", "temperature", 1)

```

For the `calculate_solution_weights` function, I wrote a helper function that parses the chemical formula and molarity from the input string. I wrote another helper function that computes the solute mass, constructs the final output, and handles the case where the chemical formula is not in our list of known molecular weights. I used `map` to map this funciton over all elements of the input list and `list` to put the values yielded by the resulting iterator into a list.

Example usage:
```
from calculate_solution_weights import calculate_solution_weights

molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

calculate_solution_weights(molecular_weights, solutions_needed)
```



"""import json

def decode_value(base, encoded_value):
    return int(encoded_value, base)

# JSON input string
json_input = '''
{
    "keys": {
        "n": 9,
        "k": 6
    },
    "1": {
        "base": "10",
        "value": "28735619723837"
    },
    "2": {
        "base": "16",
        "value": "1A228867F0CA"
    },
    "3": {
        "base": "12",
        "value": "32811A4AA0B7B"
    },
    "4": {
        "base": "11",
        "value": "917978721331A"
    },
    "5": {
        "base": "16",
        "value": "1A22886782E1"
    },
    "6": {
        "base": "10",
        "value": "28735619654702"
    },
    "7": {
        "base": "14",
        "value": "71AB5070CC4B"
    },
    "8": {
        "base": "9",
        "value": "122662581541670"
    },
    "9": {
        "base": "8",
        "value": "642121030037605"
    }
}
'''

# Load JSON data
data = json.loads(json_input)

# List to store x and y points
points = []

# Decode each point
for key in data:
    if key != "keys":
        x = int(key)  # x value is the key itself
        base = int(data[key]["base"])
        encoded_value = data[key]["value"]
        y = decode_value(base, encoded_value)  # Decode y value from the given base
        points.append((x, y))

# Display the decoded points
for x, y in points:
    print(f"(x: {x}, y: {y})")
"""
"""
from sympy import symbols, Poly, div

# Define the variable x
x = symbols('x')

# Define the points from the input
points = [
    (1, 52345), (2, 2623), (3, 814), (4, 1700)
]

# Build the Lagrange interpolating polynomial
def lagrange_interpolation(points):
    total_polynomial = 0
    for i in range(len(points)):
        xi, yi = points[i]
        li = 1
        for j in range(len(points)):
            if i != j:
                xj, _ = points[j]
                li *= (x - xj) / (xi - xj)
        total_polynomial += yi * li
    return total_polynomial

# Get the polynomial
polynomial = lagrange_interpolation(points)

# Expand the polynomial to get the coefficients
polynomial_expanded = polynomial.expand()

# Extract the constant term
constant_term = polynomial_expanded.subs(x, 0)

print(f"Interpolating Polynomial: {polynomial_expanded}")
print(f"Constant Term: {constant_term}")



"""
"""
testcase2
import json

# Define the JSON content
data = {
    "keys": {
        "n": 9,
        "k": 6
    },
    "1": {
        "base": "10",
        "value": "28735619723837"
    },
    "2": {
        "base": "16",
        "value": "1A228867F0CA"
    },
    "3": {
        "base": "12",
        "value": "32811A4AA0B7B"
    },
    "4": {
        "base": "11",
        "value": "917978721331A"
    },
    "5": {
        "base": "16",
        "value": "1A22886782E1"
    },
    "6": {
        "base": "10",
        "value": "28735619654702"
    },
    "7": {
        "base": "14",
        "value": "71AB5070CC4B"
    },
    "8": {
        "base": "9",
        "value": "122662581541670"
    },
    "9": {
        "base": "8",
        "value": "642121030037605"
    }
}

# Write the JSON data to a file
with open('testcase2.json', 'w') as file:
    json.dump(data, file, indent=4)
"""
import json

# Define the JSON content
data = {
    "keys": {
        "n": 4,
        "k": 3
    },
    "1": {
        "base": "10",
        "value": "4"
    },
    "2": {
        "base": "2",
        "value": "111"
    },
    "3": {
        "base": "10",
        "value": "12"
    },
    "6": {
        "base": "4",
        "value": "213"
    }
}

# Write the JSON data to a file
with open('testcase1.json', 'w') as file:
    json.dump(data, file, indent=4)

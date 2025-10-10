"""CLI interface for calculator operations."""

# In file: src/cli.py

"""CLI interface for calculator operations."""

import sys
import os
import click

# 💥 CRITICAL FIX: Ensure the project root is on sys.path 
# This helps pytest/CliRunner resolve imports like 'from src.calculator import...'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the calculator functions
from src.calculator import add, subtract, multiply, divide, power, square_root 

# ... the rest of your calculate function (@click.command, etc.) ...

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI supporting add, subtract, multiply, divide, power, and square_root."""
    try:
        # Check for missing operand early for two-argument operations (Page 114)
        if operation in ("add", "subtract", "multiply", "divide", "power") and num2 is None:
            raise ValueError("Missing second operand")

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root" or operation == "sqrt":
            # square_root only needs num1 (Page 114)
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
            
        # Format result cleanly to STDOUT for test verification
        if isinstance(result, (int, float)):
            # Print without decimal if it's a whole number, otherwise print with 2 decimal places
            print(int(result) if result == int(result) else f"{result:.2f}")
        else:
            print(result)

    except ValueError as e:
        # Handle specific expected errors (like division by zero, negative square root)
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
        
    except Exception as e:
        # Handle unexpected errors (Pylint flags this as W0718: broad-exception-caught)
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)
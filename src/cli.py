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
        # Check for missing operand early
        if (
            operation in ("add", "subtract", "multiply", "divide", "power")
            and num2 is None
        ):
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
        elif operation == "square_root":
            # square_root only needs num1, so we check for extra num2
            if num2 is not None:
                click.echo("Warning: Extra operand ignored for square_root.", err=True)
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Fix 1: Use standard print() to ensure the result is reliably sent to STDOUT
        # which is what the integration tests assert against.
        if isinstance(result, (int, float)):
            # Print without decimal if it's a whole number, otherwise print with 2 decimal places
            print(int(result) if result == int(result) else f"{result:.2f}")
        else:
            print(result)

    except ValueError as e:
        # Fix 2: Ensure we exit with a non-zero status code (1) on a ValueError.
        # This makes test_cli_subtract_missing_operand_error pass.
        click.echo(
            f"Error: {e}", err=True
        )  # Using err=True sends the error message to stderr
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    calculate()

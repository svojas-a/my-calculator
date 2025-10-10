"""CLI interface for calculator operations."""

import sys
import os
import click

# We remove the manual sys.path.append() here to rely on the PYTHONPATH set in ci.yml
# This is cleaner and avoids conflicts when imported as a module by pytest.

# Import the calculator functions
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI supporting add, subtract, multiply, divide, power, and square_root."""
    try:
        # Check for missing operand early for two-argument operations
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
            # square_root only needs num1
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
            
        # Format result cleanly to STDOUT for test verification
        if isinstance(result, (int, float)):
            # Use print for clean output capture by the test runner
            print(int(result) if result == int(result) else f"{result:.2f}")
        else:
            print(result)

    except ValueError as e:
        # Handle specific expected errors (like division by zero, missing operand)
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
        
    except Exception as e:
        # Handle unexpected errors
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    # Suppress pylint error for 'no-value-for-parameter' as Click handles arguments
    calculate()  # pylint: disable=no-value-for-parameter
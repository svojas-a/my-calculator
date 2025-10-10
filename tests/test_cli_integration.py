# In file: tests/integration/test_cli_integration.py

# Import CliRunner instead of subprocess (and update all test logic to use res.output/res.exit_code)
from click.testing import CliRunner 
import pytest 

# Note: We need to import calculate within run_cli to ensure proper module loading
# but you might need these basic ones for integration tests if you kept them.
# from src.calculator import add, multiply, divide, power, square_root 

class TestCLIIntegration: 
    """Test CLI application integrating with 
    calculator module (in-process)""" 

    def run_cli(self, *args): 
        """Invoke Click CLI in-process so coverage is 
        measured.""" 
        # Import CLI function here to ensure proper path loading for Pytest
        from src.cli import calculate 
        runner = CliRunner() 
        return runner.invoke(calculate, list(args)) 

    def test_cli_add_integration(self): 
        res = self.run_cli("add", "5", "3") 
        # Note the change from result.returncode to res.exit_code 
        assert res.exit_code == 0 
        # Note the change from result.stdout.strip() to res.output.strip() 
        assert res.output.strip() == "8"

    # ... (You need to update all your other integration tests 
    # to use res.exit_code, res.output.strip(), and res.output for error checking) ...

    # Example of fixed error test:
    def test_cli_subtract_missing_operand_error(self):
        res = self.run_cli('subtract', '5')
        assert res.exit_code == 1
        # Check output contains the error message, not just stdout
        assert "Missing second operand" in res.output 
        # OR: assert "Error: Missing second operand" in res.output
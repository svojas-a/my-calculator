from click.testing import CliRunner
import pytest

# You only need to import the runner and pytest here
# The necessary calculation functions are imported inside the tests where needed

class TestCLIIntegration:
    """Test CLI application integrating with calculator module (in-process)"""

    def run_cli(self, *args):
        """Invoke Click CLI in-process so coverage is measured."""
        # Import CLI function here to ensure proper path loading for Pytest
        from src.cli import calculate 
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        res = self.run_cli("add", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        res = self.run_cli("subtract", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "2"
        
    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        res = self.run_cli("multiply", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "15"
        
    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        res = self.run_cli("divide", "5", "3")
        # Assuming your CLI prints 1.67 for 5/3, based on previous context
        assert res.exit_code == 0
        assert res.output.strip() == "1.67"
        
    def test_cli_subtract_missing_operand_error(self):
        """Test CLI handles missing operand for subtraction gracefully"""
        # Call subtract with only one operand; CLI should exit with non-zero and print an error
        res = self.run_cli("subtract", "5")
        assert res.exit_code == 1
        # Check that the error output contains the expected message
        assert "Error: Missing second operand" in res.output 

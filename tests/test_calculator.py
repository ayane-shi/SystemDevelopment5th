"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestValidInput:
    def test_numbers_within_range(self):
        # Arrange
        calc = Calculator()
        values = (100, 200, -100, -200)
        expected = True

        # Act
        result = calc._validate_input(*values)

        # Assert
        assert result == expected

    def test_positive_boundary_value(self):
        """Test adding positive boundary value"""
        # Arrange
        calc = Calculator()
        values = (1000000, 100)
        expected = True

        # Act
        result = calc._validate_input(*values)

        # Assert
        assert result == expected

    def test_negative_boundary_vale(self):
        """Test adding negative boundary value"""
        # Arrange
        calc = Calculator()
        values = (-1000000, -100)
        expected = True

        # Act
        result = calc._validate_input(*values)

        # Assert
        assert result == expected

    def test_too_large_and_small_numbers(self):
        """Test adding too large nubmers"""

        # Arrange
        calc = Calculator()
        values = (1000001, 100103, -1000001, -10000212)

        with pytest.raises(InvalidInputException):
            calc._validate_input(*values)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 20
        b = 12
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 2
        b = 8
        expected = 16

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 15
        b = 3
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_zero_denominator(self):
        """Tests zero donominator"""
        # Arrange
        calc = Calculator()
        a = 15
        b = 0

        # Act
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(a, b)

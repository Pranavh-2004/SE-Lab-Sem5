import pytest
from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words

@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    """Test sanitize_string with various inputs including None."""
    try:
        result = sanitize_string(s)
        # If it succeeds, result should be a string
        assert isinstance(result, str)
    except (AttributeError, TypeError) as e:
        # Expected for None and non-string inputs
        pytest.fail(f"Expected error for input {repr(s)}: {type(e).__name__}")
    except Exception as e:
        # Catch any other unexpected errors
        pytest.fail(f"Unexpected error for input {repr(s)}: {type(e).__name__}: {e}")
    
@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    """Test parse_int_list with various inputs including None."""
    try:
        result = parse_int_list(s)
        # If it succeeds, result should be a list of integers
        assert isinstance(result, list)
        assert all(isinstance(item, int) for item in result)
    except (ValueError, AttributeError, TypeError) as e:
        # Expected for None, non-numeric strings, and invalid formats
        pytest.fail(f"Expected error for input {repr(s)}: {type(e).__name__}")
    except Exception as e:
        # Catch any other unexpected errors - this will fail the test
        pytest.fail(f"Unexpected error for input {repr(s)}: {type(e).__name__}: {e}")

@given(st.text() | st.none())
def test_reverse_words_safe(s):
    """Test reverse_words with various inputs including None."""
    try:
        result = reverse_words(s)
        # If it succeeds, result should be a string
        assert isinstance(result, str)
    except (AttributeError, TypeError) as e:
        # Expected for None and non-string inputs
        pytest.fail(f"Expected error for input {repr(s)}: {type(e).__name__}")
    except Exception as e:
        # Catch any other unexpected errors
        pytest.fail(f"Unexpected error for input {repr(s)}: {type(e).__name__}: {e}")
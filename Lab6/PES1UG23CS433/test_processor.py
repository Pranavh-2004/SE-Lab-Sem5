from hypothesis import given, strategies as st
from Lab6.PES1UG23CS433.processor_old import sanitize_string, parse_int_list, reverse_words


@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    # To-Do: Using try and except complete this function.
    try:
        sanitize_string(s)
    except Exception as e:
        assert False, f"sanitize_string raised an exception: {e}"


@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    # To-Do: Using try and except complete this function.
    try:
        parse_int_list(s)
    except Exception as e:
        assert False, f"parse_int_list raised an exception: {e}"


@given(st.text() | st.none())
def test_reverse_words_safe(s):
    # To-Do: Using try and except complete this function.
    try:
        reverse_words(s)
    except Exception as e:
        assert False, f"reverse_words raised an exception: {e}"
import pytest
from anagrams import are_anagrams

def test_basic_anagrams():
    """Test basic anagrams without spaces or case differences."""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False

def test_anagrams_with_spaces():
    """Test anagrams with spaces that should be ignored."""
    assert are_anagrams("a gentleman", "elegant man") == True
    assert are_anagrams("debit card", "bad credit") == True

def test_case_insensitivity():
    """Test that case differences are ignored."""
    assert are_anagrams("Listen", "silent") == True
    assert are_anagrams("TRIANGLE", "integral") == True

def test_non_anagrams():
    """Test strings that are not anagrams."""
    assert are_anagrams("apple", "pale") == False
    assert are_anagrams("abc", "def") == False

def test_edge_cases():
    """Test edge cases like empty strings, single characters, and identical strings."""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "a") == True
    assert are_anagrams("a", "b") == False
    assert are_anagrams("ab", "a") == False  # Different lengths
import pytest
from ..main.py import count_unique_chars

@pytest.mark.parametrize('s, expected', 
[
    ('abbbccdf', 3),
    ('', 0),
    ('aaaaaaa', 0),
    ('abcde', 5),
    ('AaBbCc', 6),
])
def test_count_unique_chars(s, expected):
    assert count_unique_chars(s) == expected

def test_type_error():
    with pytest.raises(TypeError):
        count_unique_chars(123) 
        
@pytest.mark.parametrize("input_string, expected_output", [
    ("--string abbbccdf".split(), 4),
    ("--string abcdefghijklmnopqrstuvwxyz".split(), 26),
    ("--file test.txt".split(), 3),
])
def test_main(input_string, expected_output):
    assert main(input_string) == expected_output

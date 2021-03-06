import pytest

import ssg.utils


def test_merge_dicts():
    left = {1: 2}
    right = {"red fish": "blue fish"}
    merged_expected = {1: 2, "red fish": "blue fish"}
    merged_actual = ssg.utils.merge_dicts(left, right)

    assert merged_actual == merged_expected
    assert 1 in left
    assert "red fish" not in left
    assert "red fish" in right
    assert 1 not in right


def test_required_key():
    rk = ssg.utils.required_key
    _dict = {'something': 'some_value',
             'something_else': 'other_value'}

    assert rk(_dict, 'something') == 'some_value'
    assert rk(_dict, 'something_else') == 'other_value'

    with pytest.raises(ValueError):
        rk(_dict, 'not-in-dict')

def assert_value(expected, func, **kwargs):
    actual = func(**kwargs)
    assert expected == actual, f'期望：{expected}，实际：{actual}'

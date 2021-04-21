def assert_value(expected, func, **kwargs):
    assert expected == func(**kwargs), f'期望：{expected}，实际：{func(**kwargs)}'

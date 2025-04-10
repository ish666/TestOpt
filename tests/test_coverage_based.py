from testopt.prioritization.coverage_based import prioritize_by_coverage

def test_coverage_prioritization():
    test_cases = {
        'TC1': {'L1', 'L2', 'L3'},
        'TC2': {'L3', 'L4'},
        'TC3': {'L4', 'L5'},
        'TC4': {'L6'},
    }

    result = prioritize_by_coverage(test_cases.copy())

    assert set(result) == set(test_cases.keys())
    assert result[0] == 'TC1'  # Highest unique coverage

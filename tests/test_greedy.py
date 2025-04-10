from testopt.reduction.greedy import greedy_test_suite_reduction

def test_greedy():
    test_cases = {
        'TC1': {'R1', 'R2'},
        'TC2': {'R2', 'R3'},
        'TC3': {'R3'},
        'TC4': {'R4'},
    }
    requirements = {'R1', 'R2', 'R3', 'R4'}

    result = greedy_test_suite_reduction(test_cases, requirements)
    assert set(result) == {'TC1', 'TC2', 'TC4'}

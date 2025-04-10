from testopt.prioritization.fault_based import prioritize_by_fault_history

def test_fault_based_prioritization():
    test_cases = {
        'TC1': 3,
        'TC2': 0,
        'TC3': 5,
        'TC4': 2,
    }

    result = prioritize_by_fault_history(test_cases)
    assert result == ['TC3', 'TC1', 'TC4', 'TC2']

def prioritize_by_fault_history(test_cases: dict) -> list:
    """
    Prioritize test cases based on fault detection frequency.
    Higher the fault count, higher the priority.
    """
    return sorted(test_cases, key=lambda x: test_cases[x], reverse=True)

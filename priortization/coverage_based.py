def prioritize_by_coverage(test_cases: dict) -> list:
    remaining_coverage = set()
    for coverage in test_cases.values():
        remaining_coverage.update(coverage)

    prioritized = []
    selected = set()

    while test_cases:
        best_tc = None
        best_gain = -1

        for tc, covered in test_cases.items():
            new_coverage = covered - selected
            gain = len(new_coverage)
            if gain > best_gain:
                best_gain = gain
                best_tc = tc

        if best_tc is None:
            break

        prioritized.append(best_tc)
        selected.update(test_cases[best_tc])
        del test_cases[best_tc]

    return prioritized

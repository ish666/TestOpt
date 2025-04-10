def greedy_test_suite_reduction(test_cases: dict, requirements: set) -> list:
    selected = []
    covered = set()

    while covered != requirements:
        best_case = None
        best_coverage = set()

        for tc, reqs in test_cases.items():
            new_coverage = reqs - covered
            if len(new_coverage) > len(best_coverage):
                best_case = tc
                best_coverage = new_coverage

        if best_case is None:
            break  # No more coverage possible

        selected.append(best_case)
        covered.update(test_cases[best_case])

    return selected

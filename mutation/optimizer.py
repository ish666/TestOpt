def mutation_score_optimizer(test_cases: dict, mutants: set) -> list:
    """
    Select test cases to maximize mutation coverage using a greedy strategy.
    """
    selected = []
    killed = set()

    while killed != mutants:
        best_tc = None
        best_gain = set()

        for tc, kills in test_cases.items():
            new_kills = kills - killed
            if len(new_kills) > len(best_gain):
                best_tc = tc
                best_gain = new_kills

        if not best_tc:
            break

        selected.append(best_tc)
        killed.update(test_cases[best_tc])
        del test_cases[best_tc]

    return selected

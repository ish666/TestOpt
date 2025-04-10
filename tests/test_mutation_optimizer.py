from testopt.mutation.optimizer import mutation_score_optimizer

def test_mutation_optimization():
    test_cases = {
        'TC1': {'M1', 'M2'},
        'TC2': {'M2', 'M3'},
        'TC3': {'M4'},
        'TC4': {'M3', 'M5'},
    }
    all_mutants = {'M1', 'M2', 'M3', 'M4', 'M5'}

    selected = mutation_score_optimizer(test_cases.copy(), all_mutants)
    assert set(selected) <= set(test_cases.keys())
    # Should kill all mutants
    killed = set()
    for tc in selected:
        killed.update(test_cases[tc])
    assert killed == all_mutants

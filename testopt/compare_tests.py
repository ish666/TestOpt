from testopt.prioritization.coverage_based import prioritize_by_coverage
from testopt.prioritization.fault_based import prioritize_by_fault_history
from testopt.reduction.greedy import reduce_test_suite
from testopt.defect_prediction.ml_model import DefectPredictor
from testopt.mutation.optimizer import mutation_score_optimizer

def compare_and_select_best(test_cases, mutants, defect_data):
    """
    Compare all test optimization techniques and return the best selection.
    """
    results = {}

    # Greedy Test Reduction
    reduced_suite = reduce_test_suite(test_cases)
    results['greedy'] = reduced_suite

    # Coverage-Based Prioritization
    coverage_priority = prioritize_by_coverage(test_cases.copy())
    results['coverage'] = coverage_priority

    # Fault-Based Prioritization
    fault_priority = prioritize_by_fault_history({tc: 1 for tc in test_cases})  # Assuming equal weight
    results['fault_based'] = fault_priority

    # Mutation Testing Optimization
    mutation_opt = mutation_score_optimizer(test_cases.copy(), mutants)
    results['mutation'] = mutation_opt

    # ML-Based Defect Prediction
    predictor = DefectPredictor()
    predictor.train(defect_data)
    defect_risks = predictor.predict(defect_data.drop(columns=['defective']))
    ranked_by_risk = sorted(test_cases.keys(), key=lambda tc: defect_risks[test_cases.keys().index(tc)], reverse=True)
    results['ml_based'] = ranked_by_risk

    # **Compare which method achieves the best fault coverage**
    best_method = max(results, key=lambda k: len(results[k]))  # Longest list means best fault coverage
    return best_method, results

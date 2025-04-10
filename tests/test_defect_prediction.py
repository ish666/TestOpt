import pandas as pd
from testopt.defect_prediction.ml_model import DefectPredictor

def test_defect_predictor():
    data = pd.DataFrame({
        'lines_of_code': [100, 200, 300],
        'cyclomatic_complexity': [10, 20, 30],
        'code_churn': [5, 10, 15],
        'prior_defects': [0, 1, 1],
        'defective': [0, 1, 1]
    })

    model = DefectPredictor()
    model.train(data)

    new_data = pd.DataFrame({
        'lines_of_code': [150],
        'cyclomatic_complexity': [15],
        'code_churn': [6],
        'prior_defects': [0]
    })

    probs = model.predict(new_data)
    assert 0 <= probs[0] <= 1

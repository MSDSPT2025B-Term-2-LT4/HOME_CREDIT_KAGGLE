from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score, average_precision_score, roc_auc_score
import pandas as pd
def model_evals(y_true, y_proba, cutoff = 0.5):
    """
    Returns model evaluation metrics for a binary classification model

    Parameters:
    -----------
        y_true: int (0,1) 
            Actual binary labels

        y_proba: float (between 0 and 1)
            Probability scores output of model 
        
    Returns:
    --------
        result: dict
            Dictionary of metrics and their results based on the input
                - event rate (% predicted 1's)
                - accuracy
                - roc_auc
                - pr_auc
                - recall
                - precision
                - f1
                - lift
    """

    y_pred = (y_proba > cutoff).astype(int)

    event_rate = y_pred.mean()

    accuracy = accuracy_score(y_true, y_pred)

    roc_auc = roc_auc_score(y_true, y_proba)

    pr_auc = average_precision_score(y_true, y_proba)

    recall = recall_score(y_true, y_pred)

    precision = precision_score(y_true, y_pred)

    f1 = f1_score(y_true, y_pred)

    lift = recall / event_rate

    return {'event_rate': event_rate,
            'acc': accuracy, 
            'roc_auc': roc_auc,
            'pr_auc': pr_auc, 
            'recall': recall, 
            'precision': precision, 
            'f1': f1, 
            'lift': lift}




from sklearn.model_selection import StratifiedKFold, train_test_split
import xgboost
def default_model(model, X, y, instance = 5, metric = 'pr_auc'):
   for random in [1, 2, 3, 4, 5]:
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random, stratify = y)

    xgb = xgboost.XGBClassifier(random_state = random)

    xgb.fit(X_train, y_train)

    y_test_proba = xgb.predict_proba(X_test)[:, 1]
    y_oot_proba = xgb.predict_proba(X_oot[seed_col])[:, 1]

    test_results = model_evals(y_test, y_test_proba)
    oot_results = model_evals(y_oot, y_oot_proba)

    test_score.append(test_results['pr_auc'])
    oot_score.append(oot_results['pr_auc'])

    print(f'XGBoost (Test), Random State {random}: {test_results}" ')
    print(f'XGBoost (OOT), Random State {random}: {oot_results}" ')


import numpy as np
def cutoff_perc(y_actual, y_proba, percent):
  n_cutoff = int(len(y_actual) * percent)

  scores = pd.DataFrame({'actual': y_actual, 'proba': y_proba})
  scores = scores.sort_values(by = 'proba', ascending= False)
  scores['rank'] = scores['proba'].rank(ascending = False)
  scores['ranked_pred'] = np.where(scores['rank']<= n_cutoff, 1, 0)

  print(len(scores[scores['ranked_pred'] == 1]))
  print(scores[scores['ranked_pred'] == 1]['proba'].min())
  return model_evals(y_actual, y_proba, cutoff = scores[scores['ranked_pred'] == 1]['proba'].min())



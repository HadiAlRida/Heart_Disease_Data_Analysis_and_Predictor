import warnings

from sklearn.neighbors import KNeighborsClassifier
warnings.filterwarnings('ignore')

# data wrangling & pre-processing
import pandas as pd
import numpy as np
# data training
from sklearn.model_selection import train_test_split

#model validation
from sklearn.metrics import log_loss,roc_auc_score,precision_score,f1_score,recall_score,roc_curve,auc
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,fbeta_score,matthews_corrcoef
from sklearn import metrics

# cross validation
from sklearn.model_selection import StratifiedKFold

# machine learning algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,VotingClassifier,AdaBoostClassifier,GradientBoostingClassifier,RandomForestClassifier,ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC 
from sklearn.preprocessing import MinMaxScaler
from scipy import stats
from sklearn.metrics import mean_squared_error
import xgboost as xgb
from sklearn.metrics import confusion_matrix, log_loss, accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, mean_squared_error, matthews_corrcoef




from database_handler import return_data_as_df
from lookups import InputTypes ,ChestPainType, RestECGType, StSlopeType, SexType
import pandas as pd

def data_processing(Source, drop_null=True):
  dt=pd.read_csv(Source)
  dt.columns=dt.columns.str.replace(' ', '_')

  dt['chest_pain_type'] = dt['chest_pain_type'].map({member.value: member.name for member in ChestPainType})
  dt['resting_ecg'] = dt['resting_ecg'].map({member.value: member.name for member in RestECGType})
  dt['ST_slope'] = dt['ST_slope'].map({member.value: member.name for member in StSlopeType})
  dt['sex'] = dt['sex'].map({member.value: member.name for member in SexType})
  dt.drop(dt[dt.ST_slope ==0].index, inplace=True)
  

    
  if drop_null:
        dt = dt.dropna()
  dt_numeric = dt[['age','resting_bp_s','cholesterol','max_heart_rate']]
  z = np.abs(stats.zscore(dt_numeric))
  dt = dt[(z < 3).all(axis=1)]
  return dt
def training_preprocessing(dt):
    dt = pd.get_dummies(dt, drop_first=True)
    X = dt.drop(['target'],axis=1)
    y = dt['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2,shuffle=True, random_state=5)
    scaler = MinMaxScaler()
    X_train[['age','resting_bp_s','cholesterol','max_heart_rate','oldpeak']] = scaler.fit_transform(X_train[['age','resting_bp_s','cholesterol','max_heart_rate','oldpeak']])

    return X_train, X_test, y_train, y_test
def model_building(X_train, X_test, y_train, y_test):
    classifiers = [
        ("Random Forest (Entropy)", RandomForestClassifier(criterion='entropy', n_estimators=100)),
        ("MLP", MLPClassifier()),
        ("K-Nearest Neighbors (K=9)", KNeighborsClassifier(n_neighbors=9)),
        ("Extra Trees (100 Estimators)", ExtraTreesClassifier(n_estimators=100)),
        ("XGBoost (500 Estimators)", xgb.XGBClassifier(n_estimators=500)),
        ("SVC (Linear)", SVC(kernel='linear', gamma='auto', probability=True)),
        ("SGD", SGDClassifier(max_iter=1000, tol=1e-4)),
        ("AdaBoost", AdaBoostClassifier()),
        ("Decision Tree", DecisionTreeClassifier()),
        ("Gradient Boosting", GradientBoostingClassifier(n_estimators=100, max_features='sqrt'))
    ]

    y_preds = {}

    for name, classifier in classifiers:
        classifier.fit(X_train, y_train)
        y_preds[name] = classifier.predict(X_test)

    return y_test, y_preds
def calculate_metrics(models, y_test):
    model_results = pd.DataFrame(columns=['Model', 'Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'F1 Score', 'ROC', 'Log_Loss', 'mathew_corrcoef', 'RMSE'])

    for column in models:
        CM = confusion_matrix(y_test, models[column])

        TN = CM[0][0]
        FN = CM[1][0]
        TP = CM[1][1]
        FP = CM[0][1]
        specificity = TN / (TN + FP)
        loss_log = log_loss(y_test, models[column])
        acc = accuracy_score(y_test, models[column])
        roc = roc_auc_score(y_test, models[column])
        prec = precision_score(y_test, models[column])
        rec = recall_score(y_test, models[column])
        f1 = f1_score(y_test, models[column])
        rmse = np.sqrt(mean_squared_error(y_test, models[column]))
        mathew = matthews_corrcoef(y_test, models[column])

        results = pd.DataFrame([[column, acc, prec, rec, specificity, f1, roc, loss_log, mathew, rmse]],
                               columns=['Model', 'Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'F1 Score', 'ROC', 'Log_Loss', 'mathew_corrcoef', 'RMSE'])

        model_results = model_results.append(results, ignore_index=True)

    return model_results
def feature_transformation(X_train, X_test, y_train, xgb_model):
    rf_ent = RandomForestClassifier(criterion='entropy', n_estimators=100)
    rf_ent.fit(X_train, y_train)
    y_pred_rfe = rf_ent.predict(X_test)
    
    et_100 = ExtraTreesClassifier(n_estimators=100)
    et_100.fit(X_train, y_train)
    y_pred_et_100 = et_100.predict(X_test)
    
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    
    feat_importances = pd.Series(rf_ent.feature_importances_, index=X_train.columns)
    feat_importances_2 = pd.Series(et_100.feature_importances_, index=X_train.columns)
    feat_importance_3 = pd.Series(xgb_model.feature_importances_, index=X_train.columns)
    
    feature_importances_df = pd.DataFrame({
        "Random Forest (Entropy)": feat_importances,
        "Extra Trees (100 Estimators)": feat_importances_2,
        "XGBoost (500 Estimators)": feat_importance_3
    })
    
    feature_importances_df = feature_importances_df.transpose()
    return feature_importances_df
def ml_prediction(data_source):
    # Load and preprocess the data
    dt = data_processing(data_source, drop_null=True)
    X_train, X_test, y_train, y_test = training_preprocessing(dt)

    # Train the Random Forest with entropy criterion
    rf_ent = RandomForestClassifier(criterion='entropy', n_estimators=100)
    rf_ent.fit(X_train, y_train)

    # Train an ExtraTreesClassifier
    extra_trees = ExtraTreesClassifier(n_estimators=100)
    extra_trees.fit(X_train, y_train)

    # Train an XGBoost classifier
    xgb_model = xgb.XGBClassifier()
    xgb_model.fit(X_train, y_train)

    # Make predictions on the test data
    rf_ent_predictions = rf_ent.predict(X_test)
    extra_trees_predictions = extra_trees.predict(X_test)
    xgb_predictions = xgb_model.predict(X_test)

    # Calculate evaluation metrics for each model
    rf_ent_metrics = {
        "Accuracy": accuracy_score(y_test, rf_ent_predictions),
        "Precision": precision_score(y_test, rf_ent_predictions),
        "Recall": recall_score(y_test, rf_ent_predictions),
        "F1 Score": f1_score(y_test, rf_ent_predictions)
    }

    extra_trees_metrics = {
        "Accuracy": accuracy_score(y_test, extra_trees_predictions),
        "Precision": precision_score(y_test, extra_trees_predictions),
        "Recall": recall_score(y_test, extra_trees_predictions),
        "F1 Score": f1_score(y_test, extra_trees_predictions)
    }

    xgb_metrics = {
        "Accuracy": accuracy_score(y_test, xgb_predictions),
        "Precision": precision_score(y_test, xgb_predictions),
        "Recall": recall_score(y_test, xgb_predictions),
        "F1 Score": f1_score(y_test, xgb_predictions)
    }

    # Create DataFrames for metrics
    rf_ent_metrics_df = pd.DataFrame(rf_ent_metrics, index=["Random Forest Entropy"])
    extra_trees_metrics_df = pd.DataFrame(extra_trees_metrics, index=["ExtraTreesClassifier"])
    xgb_metrics_df = pd.DataFrame(xgb_metrics, index=["XGBoost"])

    # Concatenate the DataFrames to create a single result DataFrame for metrics
    metrics_df = pd.concat([rf_ent_metrics_df, extra_trees_metrics_df, xgb_metrics_df])

    # Create confusion matrices for each model
    rf_ent_confusion = confusion_matrix(y_test, rf_ent_predictions)
    extra_trees_confusion = confusion_matrix(y_test, extra_trees_predictions)
    xgb_confusion = confusion_matrix(y_test, xgb_predictions)

    # Create a DataFrame for confusion matrices with 3 rows and 4 columns
    confusion_df = pd.DataFrame(data=[rf_ent_confusion.ravel(), extra_trees_confusion.ravel(), xgb_confusion.ravel()],
                               columns=['TN', 'FP', 'FN', 'TP'],
                               index=['Random Forest Entropy', 'ExtraTreesClassifier', 'XGBoost'])

    return metrics_df, confusion_df
def execute_ml_classification_prediction(data_source):
    dt=data_processing(data_source,drop_null=True)
    X_train, X_test,y_train,y_test=training_preprocessing(dt)
    y_test, y_preds=model_building(X_train, X_test, y_train, y_test)
    xgb_model = xgb.XGBClassifier(n_estimators=500)
    feature_importance_df=feature_transformation(X_train, X_test,y_train,xgb_model)
    models_result_df=calculate_metrics(y_preds, y_test)
    metrics_df, confusion_df= ml_prediction(data_source)

    return models_result_df,feature_importance_df,metrics_df, confusion_df



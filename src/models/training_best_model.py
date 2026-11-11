from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from src.features.preprocessing import preprocessing
from sklearn.pipeline import Pipeline
def training_best_model(model , grad_param , df):
    X = df.drop(columns=["Student_ID" , "Mental_Health_Risk"])
    Y = df["Mental_Health_Risk"]
    X_train , X_test , Y_train , Y_test = train_test_split(
        X,Y,random_state=42,test_size=0.2
    )
    preprocessor = preprocessing(X_train)
    pipline = Pipeline(steps=[
        ("preprocessor" , preprocessor),
        ("model" , model)
    ])
    gridsearch = GridSearchCV(
        pipline,
        param_grid=grad_param,
        scoring='f1_macro',
        n_jobs=-1,
        cv=5,
    )

    gridsearch.fit(X_train,Y_train)
    return (gridsearch.best_estimator_ , X_test , Y_test)


import sys
sys.path.insert(0,"../")
from src.features.preprocessing import preprocessing , Pipeline
from sklearn.model_selection import train_test_split
def training(df , model):
    X = df.drop(columns=["Student_ID" , "Mental_Health_Risk"])
    Y = df["Mental_Health_Risk"]
    X_train , X_test , Y_train , Y_test = train_test_split(
        X , 
        Y ,
        random_state=42,
        test_size=0.2
    )
    preprocessor = preprocessing(X_train)
    pipline = Pipeline(
        steps=[
            ('preprocessor' , preprocessor),
            ('model' , model)
        ]
    )
    pipline.fit(X_train , Y_train)
    return pipline , X_test , Y_test 
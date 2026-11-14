from sklearn.preprocessing import MinMaxScaler , OneHotEncoder 
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
def preprocessing(df):
    columns_categorical = df.select_dtypes(include=["object"  , "category"]).columns.tolist()
    columns_numeric = df.select_dtypes(include=["number"]).columns.tolist()
    category_pipline = Pipeline(
        steps=[
            ("impute" , SimpleImputer(strategy="most_frequent")),
            ("encoder" , OneHotEncoder(handle_unknown="ignore"))
        ]
    )
    numeric_pipline = Pipeline(steps=[
        ("impute" , SimpleImputer(strategy="mean")),
        ("encoder" , MinMaxScaler())
    ])
    preprocessor = ColumnTransformer(transformers=[
        ('num' , numeric_pipline , columns_numeric),
        ("cat" , category_pipline , columns_categorical)

    ])

    return preprocessor




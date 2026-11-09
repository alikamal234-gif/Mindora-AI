

from sklearn.metrics import accuracy_score , confusion_matrix , classification_report , matthews_corrcoef 
def evaluation(pipline , X_test , Y_test):
    Y_pred = pipline.predict(X_test)
    resultat = {
        "accuracy score : " : accuracy_score(Y_pred , Y_test),
        "confusion matrix : " : confusion_matrix(Y_pred , Y_test),
        "classification report : " : classification_report(Y_pred , Y_test),
        "matthews corrcoef : " : matthews_corrcoef(Y_pred , Y_test)
    }
    return resultat

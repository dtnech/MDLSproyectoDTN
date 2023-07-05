early_stopp = EarlyStopping(patience = 20, min_delta = 0.001, 
                                               restore_best_weights =True )
from sklearn.preprocessing import StandardScaler, LabelEncoder

escalado = StandardScaler()

x_train_escalado = escalado.fit_transform(x_train)
x_test_escalado = escalado.transform(x_test)

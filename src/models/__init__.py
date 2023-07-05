from sklearn.model_selection import train_test_split, KFold
x_train,x_test,y_train,y_test = train_test_split(x,y, stratify=y, random_state=12)
y_train.value_counts(), y_test.value_counts()
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

def create_model():
    modelo = Sequential()
    modelo.add(Dense(256,activation='relu',input_shape=[30]))
    modelo.add(Dropout(0.2))
    modelo.add(Dense(256,activation='relu'))
    modelo.add(Dropout(0.2))
    modelo.add(Dense(128,activation='relu'))
    modelo.add(Dropout(0.2))
    modelo.add(Dense(64,activation='relu'))
    modelo.add(Dropout(0.2))
    modelo.add(Dense(64,activation='relu'))
    modelo.add(Dropout(0.1))
    modelo.add(Dense(1,activation='sigmoid'))

    modelo.compile( optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
    return modelo

Modelo_clasf = create_model()
Modelo_clasf.summary()
early_stopp = EarlyStopping(patience = 20, min_delta = 0.001, 
                                               restore_best_weights =True )
from sklearn.preprocessing import StandardScaler, LabelEncoder

escalado = StandardScaler()

x_train_escalado = escalado.fit_transform(x_train)
x_test_escalado = escalado.transform(x_test)

df.info()
df.isnull().sum()
colormap = sns.color_palette("Greens")
sns.heatmap(df.isnull(), cbar=False,cmap=colormap)
f['Class'].unique()
cuenta = df.Class.value_counts()
print(cuenta)
print(f'legimate {(cuenta[0] / sum(cuenta))*100}% and Fraudent {(cuenta[1] / sum(cuenta))*100}%')
df.describe()
dfb=df.boxplot(column = ['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28'],color = 'red')
dfb.plot()
plt.show()
df[df.Class == 0].plot.scatter('Amount','Time',edgecolors="mediumaquamarine")
df[df.Class == 1].plot.scatter('Amount','Time',edgecolors="mediumaquamarine")
x = df.drop('Class', axis=1)
y = df.Class.values
#
matrix_Corr = x.corr()
plt.figure(figsize=(30,30))
sns.heatmap(matrix_Corr, annot = True,cmap="coolwarm")
plt.show()
legaldf = df[df.Class == 0]
fraudedf = df[df.Class == 1]

muestra1 = round(legaldf.shape[0] * 0.05)
muestra1

from imblearn.over_sampling import RandomOverSampler
from sklearn.utils import resample

legaldf2 = resample(legaldf, n_samples=muestra1, random_state=15)
muestra = pd.concat([legaldf2,fraudedf],axis=0)

muestrax = muestra.drop('Class', axis=1)
muestray = muestra.Class

ROS = RandomOverSampler(random_state=42)

x,y = ROS.fit_resample(muestrax,muestray)
y.value_counts()
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

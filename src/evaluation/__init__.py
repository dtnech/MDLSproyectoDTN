historico = Modelo_clasf.fit(x_train_escalado,
            y_train,
            epochs=500,
            validation_split=0.25,
            callbacks=[early_stopp],
            verbose=1)
plt.plot(historico.history['accuracy'],color = "mediumseagreen")
plt.plot(historico.history['val_accuracy'],color = "crimson")
plt.show()
y_pred = Modelo_clasf.predict(x_test_escalado)
for i in range(len(y_pred)):
    if y_pred[i] > 0.5 :
        y_pred[i] = 1
    else:
        y_pred[i] = 0
      # Created a common function to plot confusion matrix
def Plot_confusion_matrix(y, pred, model_name):
    cm = metrics.confusion_matrix(y, pred)
    plt.clf()
    plt.imshow(cm, cmap=plt.cm.Accent)
    categoria = ['No Fraude','Fraude']
    plt.title(f'Confusion Matrix - {model_name}')
    plt.ylabel('Etiquetas reales')
    plt.xlabel('Estimado')
    ticks = np.arange(len(categoria))
    plt.xticks(ticks, categoria, rotation=45)
    plt.yticks(ticks, categoria)
    s = [['TN','FP'], ['FN', 'TP']]

    for i in range(2):
        for j in range(2):
            plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]),fontsize=12)
    plt.show()
  def Plot_roc_curve(y, y_prob, model_name, score):
    plt.title(f'ROC Curve - {model_name}')
    fpr, tpr, thresholds = metrics.roc_curve(y, y_prob)
    plt.plot(fpr,tpr,label="Test, auc="+str(score))
    plt.legend(loc=4)
    plt.show()
    columnas = ['Modelo','accuracy score', ' Precision','Recall','f1_score']
evaluacion_df = pd.DataFrame(columns=columnas)
evaluacion_df
import sklearn.metrics as metrics
def print_results(model_name, y_test, y_pred, pred_prob=None):
    print(model_name)
    print('--------------------------------------------------------------------------')
 
    precision_score = metrics.precision_score(y_test, y_pred)
    recall_score = metrics.recall_score(y_test, y_pred)
    
    accuracy_score  = metrics.accuracy_score(y_test,y_pred)
    print(f'accuracy score :{accuracy_score}') 

    f1_score = metrics.f1_score(y_test,y_pred)
    
    classification_report = metrics.classification_report(y_test,y_pred)
    print(classification_report)
    
#   save scores into dataframe for comparison
    evaluacion_df.loc[len(evaluacion_df.index)] = [model_name,accuracy_score,precision_score,recall_score, f1_score]
    
    Plot_confusion_matrix(y_test,y_pred,model_name)
    
    if pred_prob is not None:
        Plot_roc_curve(y_test,pred_prob,model_name,accuracy_score)
print_results("ANN ", y_test, y_pred)
evaluacion_df

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

#loading data
data = pd.read_csv("heart_failure_clinical_records_dataset.csv")
data

data.info()

#first of all let us evaluate the target and find out if our data is imbalanced or not
cols= ["#6daa9f","#774571"]
sns.countplot(x= data["DEATH_EVENT"], palette= cols)

plt.figure(figsize=(10,10))
sns.heatmap(data.corr(), vmin=-1, cmap='coolwarm', annot=True);

data = data.dropna()
data = data.drop_duplicates()
X=data.drop(["DEATH_EVENT"],axis=1)
y=data["DEATH_EVENT"]

#Set up a standard scaler for the features
col_names = list(X.columns)
s_scaler = preprocessing.StandardScaler()
X_df= s_scaler.fit_transform(X)
X_df = pd.DataFrame(X_df, columns=col_names)

X_train, X_test, y_train,y_test = train_test_split(X_df,y,test_size=0.22,random_state=7)
X_df.describe().T

svc_clf = SVC(probability=True)
svc_clf.fit(X_train, y_train)
svc_clf_pred = svc_clf.predict(X_test)
svc_clf_acc = accuracy_score(y_test, svc_clf_pred) * 100

# Confusion Matrix
sns.heatmap(confusion_matrix(y_test, svc_clf_pred), annot=True, cmap=sns.cubehelix_palette(as_cmap=True), annot_kws = {'size':25})

rf = RandomForestClassifier(n_estimators=20, random_state=12,max_depth=5)
rf.fit(X_train,y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred) * 100

cm = confusion_matrix(y_test, rf_pred)
sns.heatmap(cm, annot=True, cmap=sns.cubehelix_palette(as_cmap=True), annot_kws = {'size':25})

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
log_reg_pred = log_reg.predict(X_test)
log_reg_acc = accuracy_score(y_test, log_reg_pred) * 100

cm = confusion_matrix(y_test, log_reg_pred)
sns.heatmap(cm, annot=True, cmap=sns.cubehelix_palette(as_cmap=True), annot_kws = {'size':25})

arr = np.array([
                [75,0,582.0,0,20.0,1,265000,1.9,130,1,0,4],
               [55.0,0,1820,0,38,0,270000.00,1.2,139,0,0,271],
                [60,1,47,0,20,0,204000,0.7,139,1,1,73],
               [50.0,0.0,196.0,0.0,45,0.0,395000.00,1.6,136.0,1,1,285.0]
])

#age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
#high_blood_pressure, platelets, serum_creatinine, serum_sodium, gender, smoking, time

#	65.0	1	160	1	20	0	327000.00	2.7	116	0	0	8  Fatal = True
# 65.0	0.0	146.0	0.0	20	0.0	162000.00	1.3	129.0	1	1	7.0 Fatal = True
# 50.0	0.0	196.0	0.0	45	0.0	395000.00	1.6	136.0	1	1	285.0  Fatal = False
arr_data = np.array([
                [75,0,582.0,0,20.0,1,265000,1.9,130,1,0,4],
                [55.0,0,1820,0,38,0,270000.00,1.2,139,0,0,271],
                [60,1,47,0,20,0,204000,0.7,139,1,1,73],
                [50.0,0.0,196.0,0.0,45,0.0,395000.00,1.6,136.0,1,1,285.0]
])
arr_data[3][0] = float(input("Enter age:"))
arr_data[3][1] = float(input("Does the patient have Anaemia?:"))
arr_data[3][2] = float(input("Enter the creatinine phosphokinase of the patient:"))
arr_data[3][3] = float(input("Does the patient have diabetes?:"))
arr_data[3][4] = float(input("Enter the ejection fraction of the patient:"))
arr_data[3][5] = float(input("Does the patient have high blood pressure?:"))
arr_data[3][6] = float(input("Enter the platelets of the patient:"))
arr_data[3][7] = float(input("Enter the serum creatinine of the patient:"))
arr_data[3][8] = float(input("Enter the serum sodium of the patient:"))
arr_data[3][9] = float(input("Enter the gender of the patient:"))
arr_data[3][10] = float(input("Does the patient smoke?:"))
arr_data[3][11] = float(input("Enter the time at which the patient has been admitted:"))
X_new= s_scaler.fit_transform(arr_data)
X_new = pd.DataFrame(X_new, columns=col_names)

y_pred = svc_clf.predict_proba(X_new)
prob_svc = y_pred[3]
y_pred = rf.predict_proba(X_new)
prob_kn = y_pred[3]
y_pred = log_reg.predict_proba(X_new)
prob_lreg = y_pred[3]


print("\nUsing Support Vector Classifier:")
print("\nProbability of a Heart Failure is %0.4f"% (prob_svc[1] * 100),"%\n\n===================================")

print("\nUsing Random Forest Classifier:")
print("\nProbability of a Heart Failure is %0.4f"% (prob_kn[1] * 100),"%\n\n===================================")

print("\nUsing Logistic Regression:")
print("\nProbability of a Heart Failure is %0.4f"% (prob_lreg[1] * 100),"%\n\n===================================")

print("\nAverage Accurate Prediction:")
sum_value = prob_svc[1] + prob_kn[1]
average = sum_value/2
print("\nProbability of a Heart Failure is %0.4f"% (average * 100),"%\n\n===================================")

risk_value = average * 100
if risk_value == 0:
  print("The patient is at no risk of heart attack.")
elif risk_value > 0 and risk_value < 25:
  print("The patient is at low risk of heart attack.")
elif risk_value > 25 and risk_value < 50:
  print("The patient is at moderate risk of heart attack.")
elif risk_value > 50 and risk_value < 75:
  print("The patient is at high risk of heart attack.")
elif risk_value > 75 and risk_value < 100:
  print("The patient is at very high risk of heart attack.")
elif risk_value == 100:
  print("The patient is at extremely high risk of heart attack.")
else:
  print("Probability value could not be read.")
  

#plt.rcParams['figure.figsize']=10,5
#sns.set_style('darkgrid')
#ax = sns.barplot(x=[ "Random Forest", "Support Vector", "Log Regression"], y=[ rf_acc, svc_clf_acc, log_reg_acc], palette = "husl", saturation =2.0)
#plt.ylabel('% of Accuracy', fontsize = 15)
#plt.title('Accuracy of Classifier Models', fontsize = 15)
#plt.xticks(fontsize = 12, horizontalalignment = 'center', rotation = 5)
#plt.yticks(fontsize = 12)
#for i in ax.patches:
 #   width, height = i.get_width(), i.get_height()
 #   x, y = i.get_xy()
 #   ax.annotate(f'{round(height,2)}%', (x + width/2, y + height*1.02), ha='center', fontsize = 'large')
#plt.show()

from sklearn import metrics
from sklearn.metrics import auc 
import numpy as np
import matplotlib.pyplot as plt
y = np.array([ 1,1,2,1,2, 2, 1])  
scores = np.array([ 0.8,0.9,0.97,0.99,0.1, 0.4, 0.35])  
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
auc = metrics.auc(fpr, tpr)
print(auc)
print(fpr,tpr)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set( ylim=[0,1.2], title='ROC',
       ylabel='TP rate', xlabel='FP')
plt.plot(fpr*len(fpr),tpr)
plt.show()
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt

filename = '../LSTM-CNN code/Accuracy-History-CNN-3class.pickle'
with open(filename, 'rb') as f:
    epoch, history_acc, history_val_acc = pickle.load(f)
epoch = [i+1 for i in epoch]
history_val_acc = [i * 100 for i in history_val_acc]
history_acc = [i * 100 for i in history_acc]

maxEpoch = np.argmax(history_val_acc)
maxAcc_val = max(history_val_acc)
maxAcc = max(history_acc)

plt.figure(1)
axes = plt.gca()
x_min = epoch[0]
x_max = epoch[-1]
axes.set_xlim([x_min, x_max])
axes.yaxis.grid(True, which='major')
axes.yaxis.grid(True, which='all')
axes.xaxis.grid(True, which='major')
axes.set_ylim([round(min(history_acc), 0), 100])

#plt.scatter(epoch, history_acc, color='r')
plt.plot(epoch, history_acc, color='r', label='Accuracy on training set')
#plt.scatter(epoch, history_val_acc, color='b')
plt.plot(epoch, history_val_acc, color='b', label='Accuracy on test set')
plt.xticks(np.arange(x_min, x_max, 2))
plt.yticks(np.arange(93, 100, 1))
plt.xlabel('Number of epochs')
plt.ylabel('Accuracy (%)')
plt.legend()
plt.savefig('Train-Test Accuracy', dpi=600)
plt.show()

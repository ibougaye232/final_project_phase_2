import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from numpy import load
from sklearn.preprocessing import LabelEncoder

data=np.load("embeddings_images_dataset.npz")

images=data["images"]
labels=data["labels"]

images2=images.reshape(105,-1)

images3=images2/255



encoder=LabelEncoder()

labels2=encoder.fit_transform(labels)

labels3=to_categorical(labels2)



mba_img=images3[0:36]
mes_img=images3[36:69]
ron_img=images3[69:105]

x_train,x_test=np.concatenate((mba_img[0:26],mes_img[0:23],ron_img[0:26]),axis=0),np.concatenate((mba_img[26:36],mes_img[23:33],ron_img[26:36]),axis=0)

mba_lab=labels3[0:36]
mes_lab=labels3[36:69]
ron_lab=labels3[69:105]

y_train,y_test=np.concatenate((mba_lab[0:26],mes_lab[0:23],ron_lab[0:26]),axis=0),np.concatenate((mba_lab[26:36],mes_lab[23:33],ron_lab[26:36]),axis=0)

print("one \n",x_train.shape)
print("two \n",x_test.shape)
print("three \n",y_train.shape)
print("four \n",y_test.shape )

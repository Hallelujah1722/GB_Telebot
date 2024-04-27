import tensorflow
import re
import string
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import keras
import os




def custom_standardization(sentence):
    # приводим в нижний регистр
    sample = tensorflow.strings.lower(sentence)
    # убираем не словесные знаки (к словесным относятся буквы, цифры и т.д.)
    sample = tensorflow.strings.regex_replace(sample, '\W', ' ')
    # убираем цифры
    sample = tensorflow.strings.regex_replace(sample, '\d', ' ')
    # убираем знаки препинания
    return tensorflow.strings.regex_replace(sample, '[%s]'%re.escape(string.punctuation), '')

data = pd.read_csv('train_Feedback/train_data.csv')
data['text'] = data['question_1'] + ', ' + data['question_2'] + ', ' + data['question_3'] + ', ' + data['question_4'] + ', ' + data['question_5']

# Разделение на обучающую и тестовую выборки
#data_train, data_test, label_train, label_test = train_test_split(data['text'], data['is_positive'], test_size=0.2, random_state=42)

data['text_len'] = data['text'].apply(lambda x: len(x.split(' ')))


max_features = 130
sequence_length = 40

vectorize_layer = keras.layers.TextVectorization(
    standardize=custom_standardization,
    split='whitespace',
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length,
    encoding='utf-8')

vectorize_layer.adapt(data['text'])

X = data['text']

Y = data["is_positive"]
X = np.array(vectorize_layer(X))

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)


embedding_dim = 9

cnn_model = keras.Sequential()
# сначала ембединг
cnn_model.add(keras.layers.Embedding(max_features+1, embedding_dim))
cnn_model.add(keras.layers.Dropout(0.2))
# далее уменьшим размерность
cnn_model.add(keras.layers.GlobalAveragePooling1D())
cnn_model.add(keras.layers.Dropout(0.2))
cnn_model.add(keras.layers.Dense(16, activation='relu'))
# слой для вывода результата. сигмоида для того, чтобы попасть в рамки [0, 1]
# в остальных моделях последним слоем также будет сигмоида
cnn_model.add(keras.layers.Dense(1, activation='sigmoid'))

cnn_model.compile(loss='binary_crossentropy',
             optimizer=keras.optimizers.Adam(),
             metrics=['accuracy'])

checkpoint_path = os.path.realpath(__file__).split("neiron.py")[0] + 'neirmodels/cp.weights.h5'
# Create a callback that saves the model's weights
cp_callback =keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)

Method = "learn"
if Method == "learn":
    cnn_model.fit(X_train, y_train, epochs=3,batch_size=512,callbacks=[cp_callback], validation_data=(X_test, y_test),verbose=1)

    print('Модель сохранена в /neirmodels')
elif Method == "work":
    print("Загрузка последней сохраненной модели")
    cnn_model.load_weights(checkpoint_path)
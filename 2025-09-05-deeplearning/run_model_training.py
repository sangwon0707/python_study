import numpy as np
import pandas as pd
from keras.utils import to_categorical
from keras import Sequential, layers, optimizers

# 1. 데이터 로딩
file_path_normal = "C:/project_personal/python_test/2025-09-05-deeplearning/dataset/ptbdb_normal.csv"
file_path_abnormal = "C:/project_personal/python_test/2025-09-05-deeplearning/dataset/ptbdb_abnormal.csv"
data_normal = pd.read_csv(file_path_normal)
data_abnormal = pd.read_csv(file_path_abnormal)

# 2. 데이터 전처리
data_normal = np.array(data_normal)
data_abnormal = np.array(data_abnormal)

# 데이터셋 분할 (학습용, 테스트용)
nTrain = 3000
nTest = 1000

# 특징(X)과 라벨(Y) 분리 및 데이터셋 생성
# 마지막 열은 라벨이므로 특징(X)에서는 제외합니다.
x_train = np.concatenate((data_normal[:nTrain, :-1], data_abnormal[:nTrain, :-1]), axis=0)
x_test = np.concatenate((data_normal[nTrain:nTrain+nTest, :-1], data_abnormal[nTrain:nTrain+nTest, :-1]), axis=0)

y_train = np.concatenate((np.zeros(nTrain), np.ones(nTrain)), axis=0)
y_test = np.concatenate((np.zeros(nTest), np.ones(nTest)), axis=0)

# 라벨을 원-핫 인코딩으로 변환
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Conv1D 입력을 위해 데이터에 채널 차원 추가 (3D로 변환)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# 3. 모델 정의 및 컴파일
model = Sequential()

model.add(layers.Conv1D(filters=16, kernel_size=3, input_shape=(x_train.shape[1], 1), activation='relu'))
model.add(layers.Conv1D(filters=16, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling1D(pool_size=3, strides=2))

model.add(layers.Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(layers.Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling1D(pool_size=3, strides=2))

model.add(layers.LSTM(16))

model.add(layers.Dense(units=2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.Adam(learning_rate=0.01),
              metrics=['accuracy'])

model.summary()

# 4. 모델 학습
print("\n--- 모델 학습 시작 ---")
history = model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.2)

# 5. 모델 평가
print("\n--- 모델 평가 ---")
loss, accuracy = model.evaluate(x_test, y_test)
print(f"테스트 데이터 정확도: {accuracy*100:.2f}%")

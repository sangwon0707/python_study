# 딥러닝 모델 생성 템플릿 (나만의 치트 시트)

# --- 0. 기본 도구 불러오기 ---
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, models

# --- 1. 재료 손질 (데이터 준비) ---

# 1-1. 데이터 불러오기 (예: MNIST)
# 다른 데이터셋을 사용하려면 이 부분을 바꾸세요. (예: fashion_mnist)
(X_train, Y_train_class), (X_test, Y_test_class) = keras.datasets.mnist.load_data()

# 1-2. 데이터 모양 맞추기 (2D -> 1D)
# 이미지 크기가 28x28이 아니라면 784 대신 다른 값을 사용하세요.
X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

# 1-3. 값의 범위 조절하기 (정규화)
X_train = X_train / 255
X_test = X_test / 255

# 1-4. 정답 형식 맞추기 (원-핫 인코딩)
# 분류할 클래스(정답)의 개수가 10개가 아니라면 10 대신 다른 값을 사용하세요.
Y_train = keras.utils.to_categorical(Y_train_class, 10)
Y_test = keras.utils.to_categorical(Y_test_class, 10)


# --- 2. 그릇 준비 & 3. 내용물 채우기 (모델 설계) ---

model = models.Sequential()
# 입력층: 입력 데이터의 모양(784)을 알려줍니다.
model.add(layers.Input(shape=(784,)))
# 은닉층: 뉴런 개수(예: 512)와 활성화 함수를 지정합니다. 이 층을 여러 개 쌓을 수도 있습니다.
model.add(layers.Dense(512, activation='relu'))
# 출력층: 최종적으로 분류할 클래스 개수(10)와 확률을 계산해주는 'softmax'를 지정합니다.
model.add(layers.Dense(10, activation='softmax'))

# 모델 구조 한눈에 보기
model.summary()


# --- 4. 요리 방법 설정 (모델 컴파일) ---

model.compile(
    optimizer='adam', # 어떻게 학습할 것인가 (대부분 adam으로 시작하면 좋습니다)
    loss='categorical_crossentropy', # 정답과 얼마나 다른지 측정하는 방법
    metrics=['accuracy'] # 학습 과정을 무엇으로 평가할 것인가 (정확도)
)


# --- 5. 오븐에 굽기 (모델 학습 및 평가) ---

print("\n--- 모델 학습 시작 ---")
# 학습 실행: epochs는 전체 데이터를 몇 번 반복 학습할지, batch_size는 한 번에 몇 개씩 학습할지를 의미합니다.
history = model.fit(
    X_train, 
    Y_train, 
    epochs=5, 
    batch_size=128, 
    validation_split=0.2 # 학습 데이터 중 20%를 검증용으로 사용
)

print("\n--- 모델 평가 ---")
# 시험용 데이터로 최종 성능 평가
loss, accuracy = model.evaluate(X_test, Y_test)
print(f"최종 정확도: {accuracy*100:.2f}%")


# --- (선택) 특정 데이터로 예측해보기 ---

print("\n--- 새로운 데이터로 예측 ---")
# 시험용 데이터의 첫 번째 이미지로 예측
predictions = model.predict(X_test[:1])
# 예측 결과 중 가장 확률이 높은 숫자의 인덱스를 찾음
predicted_number = np.argmax(predictions[0])
actual_number = Y_test_class[0]

print(f"모델의 예측: {predicted_number}")
print(f"실제 정답: {actual_number}")

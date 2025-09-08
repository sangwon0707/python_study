# `Untitled-2.ipynb` 코드 설명

이 Jupyter Notebook 파일은 시간별 대기질 데이터를 분석하고, 그 결과를 시각화한 뒤, 생성된 이미지를 딥러닝 모델을 통해 분류하는 과정을 담고 있습니다.

전체 과정은 다음과 같이 요약할 수 있습니다.

1.  **데이터 로딩 및 전처리**: 시간별 대기질 데이터(CSV)를 불러와 Pandas DataFrame으로 다루기 쉽게 가공합니다.
2.  **데이터 시각화**: 일별 미세먼지(PM10) 농도 변화를 그래프로 그리고, 각 그래프를 이미지 파일(.png)로 저장합니다.
3.  **이미지 처리**: 저장된 이미지 파일 중 하나를 딥러닝 모델의 입력 형식에 맞게 (예: 28x28 픽셀) 변환합니다.
4.  **모델 예측**: 미리 학습된 Keras 모델을 불러와, 처리된 이미지가 어떤 클래스에 속하는지 예측합니다.

## 1. 데이터 로딩 및 전처리

먼저, 분석에 필요한 라이브러리들을 가져옵니다.

```python
from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
```

`amb_hour_time.csv` 파일을 Pandas DataFrame으로 읽어옵니다. 이 데이터는 시간별 'PM10', 'PM2.5' 등 대기질 측정값을 포함하고 있습니다.

```python
file_path = 'C:/project_personal/python_test/2025-09-06/dataset/amb_hour_time.csv'
df = pd.read_csv(file_path)
```

`df.info()`를 통해 데이터의 기본 정보를 확인합니다. 'date' 컬럼이 문자열(object) 타입인 것을 알 수 있습니다.

시간 데이터를 다루기 쉽도록 `pd.to_datetime` 함수를 사용해 'date' 컬럼을 datetime 객체로 변환하고 'new_date'라는 새로운 컬럼에 저장합니다.

```python
df['new_date'] = pd.to_datetime(df['date'])
```

'new_date' 컬럼에서 날짜(date)와 시간(hour) 정보를 각각 추출하여 기존 'date' 컬럼과 새로운 'hour' 컬럼에 저장합니다.

```python
df['date'] = df['new_date'].dt.date
df['hour'] = df['new_date'].dt.hour
```

## 2. 데이터 시각화

일별 PM10 농도 변화를 그래프로 그리는 `plot_df` 함수를 정의합니다. 이 함수는 그래프를 그리고, 해당 날짜를 제목으로 하여 `.png` 파일로 저장하는 역할을 합니다.

```python
def plot_df(df, x, y, title="", xlabel='hour', ylabel='PM10', dpi=100):
    plt.figure(figsize=(5,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.gca().axes.xaxis.set_visible(False)
    plt.ylim(0,100)

    pic_name = title + ".png"
    plt.savefig(pic_name)

    plt.show()
```

반복문을 통해 전체 데이터에 대해 하루(24시간) 단위로 PM10 농도 그래프를 생성하고 이미지 파일로 저장합니다.

```python
for x in range(24):
    plot_df(
        df,
        x=df.hour[x*24:(x+1)*24],
        y=df.PM10[x*24:(x+1)*24],
        title=str(df.date[x*24])
    )
```

## 3. 이미지 처리 및 모델 입력 준비

시각화를 통해 생성된 이미지 중 하나(`2022-05-24.png`)를 불러옵니다.

OpenCV(`cv2`)를 사용하여 이미지를 흑백(grayscale)으로 읽고, 그래프 영역만 남도록 자른 뒤 `newimg.png`로 저장합니다.

```python
img2 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
newimg = img2[65:445, 65:445]
cv2.imwrite("newimg.png", newimg)
```

딥러닝 모델의 입력으로 사용하기 위해, 잘라낸 이미지를 28x28 픽셀 크기로 재조정(resize)합니다. 이는 MNIST와 같은 이미지 분류 모델에서 흔히 사용되는 이미지 크기입니다.

```python
img3 = cv2.imread('newimg.png', cv2.IMREAD_GRAYSCALE)
img3 = cv2.resize(img3, (28, 28))
```

## 4. 모델 예측

미리 학습된 Keras 모델(`myFMNIST.h5`)을 불러옵니다. `model.summary()`를 통해 모델의 구조를 확인할 수 있습니다.

```python
model = keras.models.load_model('myFMNIST.h5')
model.summary()
```

### `model.summary()` 결과 분석

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ flatten_1 (Flatten)             │ (None, 784)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 128)            │       100,480 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 64)             │         8,256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_4 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 10)             │           330 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 111,148 (434.18 KB)
 Trainable params: 111,146 (434.16 KB)
 Non-trainable params: 0 (0.00 B)
 Optimizer params: 2 (12.00 B)
```

위 표는 모델의 구조를 보여줍니다.

- **Layer (type) / Output Shape / Param #**: 각 층의 종류, 출력 데이터의 형태, 학습 파라미터 수를 나타냅니다.
    - **flatten_1 (Flatten)**: 첫 번째 층으로, 2차원 이미지 데이터(28x28 픽셀)를 1차원 배열(784개 원소)로 평탄화합니다. 학습 파라미터는 없습니다.
    - **dense_2 (Dense)**: 128개의 뉴런을 가진 완전 연결 계층입니다. Flatten 층에서 나온 784개의 입력을 받아 128개의 출력으로 변환합니다. 파라미터 수는 `(입력 뉴런 수 784 * 출력 뉴런 수 128) + 편향 128 = 100,480`개 입니다.
    - **dense_3 (Dense)**: 64개의 뉴런을 가진 층입니다.
    - **dense_4 (Dense)**: 32개의 뉴런을 가진 층입니다.
    - **dense_5 (Dense)**: 마지막 출력층으로, 10개의 뉴런을 가집니다. 각 뉴런은 10개의 최종 분류(Type1~Type10)에 대한 예측 확률 점수를 나타냅니다.

- **Total params**: 모델의 모든 파라미터 개수의 총합입니다.
- **Trainable params**: 훈련 과정에서 역전파를 통해 가중치가 업데이트되는, 즉 **학습이 진행되는** 파라미터의 총 개수입니다. 이 모델에서는 대부분의 파라미터가 학습 대상입니다.
- **Non-trainable params**: 훈련 과정에서 값이 업데이트되지 않도록 동결(freeze)된 파라미터의 개수입니다. 주로 전이 학습(Transfer Learning) 시에 기존 학습된 가중치를 그대로 사용하기 위해 설정합니다. 이 모델에서는 0개입니다.
- **Optimizer params**: 모델 자체의 파라미터는 아니지만, Adam, SGD 등과 같은 옵티마이저가 훈련 상태를 유지하기 위해 사용하는 파라미터의 개수입니다.

---

모델이 예측을 수행할 수 있도록, 28x28 크기의 이미지에 배치(batch) 차원을 추가하여 `(1, 28, 28)` 형태로 만듭니다.

```python
input_data = img3[np.newaxis, :, :]
```

마지막으로, 모델의 `predict` 함수를 호출하여 이미지를 분류합니다. `np.argmax`를 통해 가장 확률이 높은 클래스의 인덱스를 얻고, `class_name` 리스트를 참조하여 해당 클래스의 이름을 출력합니다.

```python
class_name = ['Type1', 'Type2', 'Type3', 'Type4', 'Type5', \
              'Type6', 'Type7', 'Type8', 'Type9', 'Type10']
y = np.argmax(model.predict(input_data))
print(class_name[y])
```

결과적으로 이 코드는 '2022-05-24'의 PM10 농도 그래프 이미지를 'Type9'으로 예측합니다.

```
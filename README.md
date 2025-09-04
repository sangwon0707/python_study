# Python Study Project

이 저장소는 Python 학습 과정을 기록하는 프로젝트입니다.

## 목차

- [2025-09-01](#2025-09-01) - Python 기초 문법
- [2025-09-02](#2025-09-02) - Python 중급 문법
- [2025-09-03](#2025-09-03) - Python 반복문, 함수
- [2025-09-04](#2025-09-04) - Numpy와 Pandas 기초

---

## 2025-09-01
Python 변수, 출력, 입력, 형변환, 산술연산자 기초 문법 학습

## 2025-09-02
Python 수학함수(math 모듈), 문자열 처리, 관계/논리 연산자, 조건문(if/elif/else), 반복문(while/for) 기초 및 중급 문법 학습

## 2025-09-03
다양한 예제를 통한 반복문(for, while) 심화 학습, 함수와 프로시저의 정의 및 활용, 전역/지역 변수의 범위(scope) 이해

## 2025-09-04

오늘은 Python에서 데이터 핸들링의 핵심 라이브러리인 **Numpy**와 **Pandas**에 대해 학습했습니다. 이 두 라이브러리는 데이터를 효율적으로 불러오고, 가공하며, 분석하는 데 필수적인 도구입니다.

### 1. Numpy: 파이썬의 과학 계산 핵심 라이브러리

Numpy는 다차원 배열(ndarray) 객체를 중심으로 빠른 수치 연산을 지원합니다.

#### 가. 배열 생성 및 변형 (`reshape`)

Numpy 배열은 `np.array()`로 생성하며, `.reshape()`를 사용해 데이터의 총 개수는 유지하면서 배열의 형태(shape)를 변경할 수 있습니다. 이는 이미지 데이터 처리나 딥러닝 모델의 입력 데이터를 준비할 때 매우 유용합니다.

- **주요 개념**:
  - `reshape(-1, n)`: 열(column)의 수를 `n`으로 고정하고 행(row)의 수는 자동으로 계산하도록 합니다.
  - 차원의 순서는 가장 큰 단위부터 작은 단위 순으로 구성됩니다. 예를 들어, `(2, 2, 3)`은 3개의 원소를 가진 2x2 행렬이 2개 있다는 의미입니다.

```python
import numpy as np

# 1차원 배열을 1x3 형태의 2차원 배열로 변경
C = np.array([1, 2, 3])
C_reshaped = C.reshape(1, 3)
# C.shape: (3,) -> C_reshaped.shape: (1, 3)

# 2x3 배열을 3x2 배열로 변경
D = np.array([[1, 2, 3], [4, 5, 6]])
D_reshaped = D.reshape(3, 2)
# D.shape: (2, 3) -> D_reshaped.shape: (3, 2)
```

#### 나. 인덱싱(Indexing)과 슬라이싱(Slicing)

배열의 특정 위치에 있는 원소나 원하는 부분집합을 추출할 수 있습니다.

- **Indexing**: `A[행, 열]` 형태로 특정 원소에 접근합니다.
- **Slicing**: `:`을 사용하여 특정 범위의 행이나 열을 가져옵니다. `A[:, 0]`은 모든 행의 첫 번째 열을 의미합니다.

```python
import numpy as np

A = np.array([[10, 20], [30, 40], [50, 60]])

# 인덱싱: 2행 1열의 원소 접근
element = A[2, 1]  # 60

# 슬라이싱: 모든 행의 첫 번째 열 데이터 추출
column_data = A[:, 0]  # array([10, 30, 50])
```

### 2. Pandas: 파이썬 데이터 분석의 필수 도구

Pandas는 Series와 DataFrame이라는 데이터 구조를 제공하여, 테이블 형태의 데이터를 다루는 데 최적화되어 있습니다.

#### 가. 데이터 선택 및 필터링 (`loc` vs `iloc`)

DataFrame에서 원하는 데이터를 정확하고 명확하게 추출하기 위해 `loc`와 `iloc`를 사용하는 것이 중요합니다.

- **`loc` (Label-based indexing)**: 인덱스의 이름(label)을 기준으로 데이터를 선택합니다. `df.loc[인덱스이름, 컬럼이름]` 형태로 사용합니다.
- **`iloc` (Integer-based indexing)**: 인덱스의 정수 위치(0부터 시작)를 기준으로 데이터를 선택합니다. `df.iloc[행번호, 열번호]` 형태로 사용합니다.

> **왜 `loc`/`iloc`를 사용할까?**
> `df[...]`와 같은 기본 인덱싱은 행을 선택하는지, 열을 선택하는지 모호할 때가 있습니다. `loc`와 `iloc`는 각각 이름과 위치를 명확히 지정하므로 코드의 가독성과 안정성을 크게 높여줍니다.

```python
import seaborn as sns

tips = sns.load_dataset("tips")

# loc: 인덱스 이름이 0부터 3인 행의 'total_bill', 'day' 컬럼 선택
data_loc = tips.loc[0:3, ['total_bill', 'day']]

# iloc: 0번부터 3번 행까지(4개), 0번부터 1번 열까지(2개) 선택
data_iloc = tips.iloc[0:4, 0:2]
```

#### 나. 조건부 데이터 선택

논리 연산자(`&`, `|`, `~`)를 사용해 복잡한 조건에 맞는 데이터를 쉽게 필터링할 수 있습니다.

```python
# 팁(tip)이 5달러 이상인 데이터만 추출
high_tip = tips[tips['tip'] > 5]

# 성별이 남성이면서, 비흡연자인 데이터 추출
male_non_smoker = tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'No')]

# isin: 팁을 1, 3, 5달러 중 하나로 지불한 데이터 추출
tip_isin = tips[tips['tip'].isin([1, 3, 5])]
```

#### 다. 데이터프레임 병합 (`merge`)

여러 DataFrame을 특정 기준(키)에 따라 합칠 수 있습니다. SQL의 `JOIN`과 유사한 기능입니다.

- **`inner join`**: 두 DataFrame에 공통으로 존재하는 키 값에 해당하는 데이터만 합칩니다. (데이터 무결성 확보에 유리)
- **`outer join`**: 두 DataFrame 중 한쪽에만 키가 존재하더라도 모든 데이터를 포함하여 합칩니다. 일치하는 데이터가 없는 경우 `NaN`으로 표시됩니다. (최대한 많은 데이터 확보에 유리)

```python
import pandas as pd

# 고객 정보 df1과 주문 정보 df2를 '고객번호' 기준으로 병합
merged_inner = pd.merge(df1, df2, how='inner', on='고객번호')
merged_outer = pd.merge(df1, df2, how='outer', on='고객번호')
```

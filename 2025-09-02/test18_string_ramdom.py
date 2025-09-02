'''
랜덤 단어 생성하기 
1. 다섯개의 문자로 이루어진 랜덤 단어를 출력한다.
2. 소문자 상수를 가져온다. 
3. 임의의 문자를 선택한다.
4. 결과를 출력한다. 
'''

import random
import string

alphabet = string.ascii_lowercase

random_word = alphabet[random.randrange(26)] + \
        alphabet[random.randrange(26)] + \
        alphabet[random.randrange(26)] + \
        alphabet[random.randrange(26)] + \
        alphabet[random.randrange(len(alphabet))]

print(random_word)
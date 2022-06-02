from graphlib import TopologicalSorter

ts = TopologicalSorter()

ts.add('영어 중급', '영어 초급')
ts.add('영어 고급', '영어 중급')

ts.add('영어 문법', '영어 중급')
ts.add('영어 고급', '영어 문법')

ts.add('영어 회화', '영어 문법')

ts.add('비즈니스 영어 회화', '영어 회화')

ts.add('영어 어원의 발전', '영어 문법', '영어 단어')

# ts.add('영어 문법', '영어 고급')  # Cycle Error

print(list(ts.static_order()))
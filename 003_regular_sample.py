data = """
홍길동의 주민 등록 번호는 800101-1055231 입니다.
그리고 고길동의 주민 등록 번호는 781011-1012411 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7].isdigit():
            word = word[:6] + "-" + "********"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


import re
print("================================================")
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

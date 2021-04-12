# Start

## 표준 입출력

```python
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

text = input()
print(text)
```

* 실행 콘솔(입출력 창)과 프로그램 간의 연결을 std, 스탠다드 스트림
* `sys.stdin`으로 콘솔과 연결하는 것이 아니라 input.txt와 프로그램 간 연결
  * 파이참 입력 버퍼 약 1MB
  * 큰 파일을 처리할 때, 1MB가 넘어가는 입력 값을 처리할 때 사용
* `sys.stdout` 으로 콘솔과 연결하는 것이 아니라 output.txt와 프로그램 간 연결
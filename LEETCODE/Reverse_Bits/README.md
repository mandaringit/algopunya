# [LEETCODE] Reverse Bits

비트 뒤집기

### 접근

32비트라고 할 때, 비트가 주어지면 이를 거꾸로(101100 -> 001101) 뒤집은 수를 출력해야한다.

0에서 시작, 32번 반복한다.

1. 답을 왼쪽으로 한번 쉬프트하고,(001-> 0010) n의 끝자리와 OR 연산. (0010 & 1 -> 0011)
2. n을 오른쪽으로 한번 쉬프트하자. (101100 -> 010110, 끝자리를 맞추기 위함이다.)

- 자바스크립트에선 비트연산자(`<<`,`|`)가 32bit-signed int를 강제한다. 때문에 32비트 숫자가 1인 경우 음수가 나와 테스트에 실패한다. `*=`을 사용하면 js float 형식을 강제하기 때문에(53비트 까지 가능) 충분하다.

_JavaScript Uses 32 bits Bitwise Operands_
JavaScript stores numbers as 64 bits floating point numbers, but all bitwise operations are performed on 32 bits binary numbers.

Before a bitwise operation is performed, JavaScript converts numbers to 32 bits signed integers.

After the bitwise operation is performed, the result is converted back to 64 bits JavaScript numbers.

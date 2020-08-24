# [LEETCODE] Duplicate Zeros

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

#### 기존 배열 변환 없이 삽입

0을 만나면 뒤에 0을 하나 추가하고 나머지를 한칸씩 뒤로 옮겨야 하는데, 그냥 그대로 했다가 시간초과가 났다. 아마 뒤에 [0,0,0,0,0] 과 같이 된 부분 부터는 더이상 작업을 할 필요가 없기때문인것 같다.

배열이 가지고 있는 메서드를 써도 (js같은 경우 `splice`로 사이에 집어넣고 마지막 요소를 뺀다던지) 쉽게 가능하긴 하다. 원본을 변경하는것이 핵심..

다만 인덱스로 구현 해보는것이 작동 원리를 알아보기 위해선 괜찮은 시도였던것 같다.

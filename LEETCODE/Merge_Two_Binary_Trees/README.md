# [LEETCODE] Merge Two Binary Trees

두개의 이진트리 합치기

### 접근

똑같은 자리를 동일하게 타고 내려가면서 값을 확인하고 이를 합치면 된다. 다만 이게 None인 노드들과의 비교가 되기 때문에 and 연산자로 확인해줘야할 필요가 있다.

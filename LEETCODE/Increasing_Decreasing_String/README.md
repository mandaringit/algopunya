# [LEETCODE] Increasing Decreasing String

문자열이 주어졌을때, 중복없는 알파벳의 오름차순 정렬 문자열 + 내림차순 정렬 문자열을 반복해 정렬한 문자열 반환

### 접근

처음엔 너무 오래걸릴까 싶긴 했는데 많아봐야 O(N)이다. 알파벳도 많아봐야 26이니까 크게 문제 안됨

1. 문자를 map에 순서대로 저장(중요)하고 알파벳을 카운팅한다. (dict가 ordered_dict여야 함.)
2. 오름차순인지 내림차순인지 체크하고 이에 따라 키를 알파벳 순서 또는 역순으로 루프하면서 키의 값이 1 이상이면 단어를 만들기 위해 모은다. 그리고 1 감소 후 0 이하인 경우엔 키를 아예 지운다. (다음 루프를 줄이기 위해)
3. 모은 단어를 합친다.
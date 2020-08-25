# [LEETCODE] Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

### 업다운 게임

결과를 특정 함수에 넣으면 알려주기 때문에 이를 토대로 검색 범위를 변경하면 되는 문제다. 일반 이진탐색과 크게 다를거 없다.

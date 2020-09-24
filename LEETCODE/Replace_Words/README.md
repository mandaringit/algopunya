# [LEETCODE] Replace Words

주어진 문장의 특정 단어에 dictionary에 있는 root가 존재한다면 해당 단어를 successor를 제외한 root로 변경하여 다시 구성한 문장을 구하는 함수를 구현하라.

### 접근

다소 복잡하게 느껴질 수도 있지만 Trie를 활용한 간단한 문제이다.

1. Trie 자료구조를 활용하여 dictionary의 단어들을 먼저 저장하도록 한다.
2. 바꿔야할 문장인 sentence를 공백을 기준으로 나눈 뒤 각 단어를 순회한다.
3. 순회하는 각 단어들을 Trie에서 찾다가 dictionary에 있었던 단어가 나온다면 (`node['is_word'] = True`) 지금까지 타고 내려온 노드들의 알파벳을 합쳐 리턴해준다.
4. 만약 없다면 기존 단어를 그대로 리턴.

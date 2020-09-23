# [LEETCODE] Implement Trie(Prefix Tree)

Trie 구현하기

### 접근

Trie의 개념을 이해하고 이를 구현하면 된다. 구현시에 'abc'라는 단어가 있다면, Trie를 이렇게 구현해 봤는데 각 string을 슬라이싱하기 때문에 속도 면에서 다소 느린 감이 있었다.

```py
{
  'a': {
    'ab':{
      'abc':{}
    }
  }
}
```

때문에 그냥 character 단위로 저장하는게 더 낫다고 보인다. 어차피 단어인지 여부는 flag를 하나 넣어서 판단하면 된다.

> 완성된 단어인지 아닌지 여부도 확인

```py
{
  'a': {
    'is_word' : False,
    'b':{
      'is_word' : False,
      'c':{
        'is_word' : True,
      }
    }
  }
}
```

TrieNode를 클래스로 구현해서 사용하는 방법도 있다.

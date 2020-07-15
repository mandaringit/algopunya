function solution(clothes) {
  let answer = 0;

  const clothesMap = new Map();
  // 분류 먼저 하고
  for (let i = 0; i < clothes.length; i++) {
    const cloth = clothes[i];
    const name = cloth[0];
    const type = cloth[1];

    if (clothesMap.has(type)) {
      clothesMap.set(type, [...clothesMap.get(type), name])
    } else {
      clothesMap.set(type, [name])
    }
  }

  for (let i = 1; i < 1 << clothesMap.size; i++) {
    let count = 1;
    for (let j = 0; j < clothesMap.size; j++) {
      if (i & (1 << j)) {
        const key = [...clothesMap.keys()][j];
        count *= clothesMap.get(key).length
      }
    }

    answer += count
  }

  return answer;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

function solution(clothes) {
  let answer = 1;
  const clothesObj = {};
  // 분류 먼저 하고
  for (let i = 0; i < clothes.length; i++) {
    const cloth = clothes[i];
    const name = cloth[0];
    const type = cloth[1];

    if (clothesObj[type]) {
      clothesObj[type].push(name);
    } else {
      clothesObj[type] = [name];
    }
  }

  for (let key in clothesObj) {
    answer *= (clothesObj[key].length + 1)
  }

  return answer - 1;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

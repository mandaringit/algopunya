function solution(n, computers) {
  let count = 0;
  let visited = Array(n).fill(0);

  function makeNetwork(i) {
    visited[i] = 1;
    for (let ni = 0; ni < n; ni++) {
      // 자기자신은 아니고, 그다음놈이 방문한것도 아니고, 연결되어 있으면
      if (ni !== i && visited[ni] === 0 && computers[i][ni] === 1 ) {
        makeNetwork(ni);
      }
    }
  }

  // 각자 출발점으로 dfs / bfs
  for (let i = 0; i < n; i++) {
    if (visited[i] === 0){
      count += 1;
      makeNetwork(i)
    }
  }

  return count;
}

console.log(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]));
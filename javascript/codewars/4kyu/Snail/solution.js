snail = function (array) {
  const N = array[0].length;
  const result = [];
  const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  let dIdx = 0;
  let x = 0;
  let y = 0;

  for (let i = 0; i < N * N; i++) {
    // 지금 자리를 넣고
    result.push(array[x][y]);
    // 지금 자리를 빈공간으로 전환
    array[x][y] = null;

    // 다음 자리를 본다.
    let [dx, dy] = d[dIdx];
    let nx = x + dx;
    let ny = y + dy;

    // 다음 자리가 벽이면 방향을 바꾼 이후의 자리를 x,y로, 아니면 그대로.
    if (nx < 0 || nx >= N || ny < 0 || ny >= N || !array[nx][ny]) {
      dIdx += 1;
      dIdx %= 4;
    }

    [dx, dy] = d[dIdx];
    x = x + dx;
    y = y + dy;
  }
  return result;
}


snail([[]])
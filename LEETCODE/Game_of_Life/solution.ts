/**
 Do not return anything, modify board in-place instead.
 */
function gameOfLife(board: number[][]): void {
  if (board.length === 0) return;

  const d = [
    [-1, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
  ];

  // 0 -> dead
  // 1 -> live
  // 2 -> dead but next live
  // 3 -> live but next dead
  const R = board.length;
  const C = board[0].length;

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      let live_neighbors = 0;

      for (let [dx, dy] of d) {
        const ni = i + dx;
        const nj = j + dy;
        if (ni >= 0 && ni < R && nj >= 0 && nj < C) {
          if ([1, 3].includes(board[ni][nj])) live_neighbors++;
        }
      }

      const cell = board[i][j];
      if (cell === 1) {
        if (live_neighbors < 2 || live_neighbors > 3) {
          board[i][j] = 3;
        }
      } else {
        if (live_neighbors === 3) board[i][j] = 2;
      }
    }
  }

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      const cell = board[i][j];
      if (cell === 2) board[i][j] = 1;
      if (cell === 3) board[i][j] = 0;
    }
  }
}

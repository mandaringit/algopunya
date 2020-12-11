/**
 Do not return anything, modify matrix in-place instead.
 */

function rotate(matrix: number[][]): void {
  const N = matrix.length;

  // 상하 뒤집기
  for (let i = 0; i < Math.trunc(N / 2); i++) {
    for (let j = 0; j < N; j++) {
      const temp = matrix[i][j];
      matrix[i][j] = matrix[N - 1 - i][j];
      matrix[N - 1 - i][j] = temp;
    }
  }

  // 대칭시키기
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (i > j) {
        const temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
      }
    }
  }
}

// 얼마나 많은 4인 가족이 앉을 수 있을까 ?
// 4인은 나눠질땐 2인 - 2인 으로 나눠져야 함
// 3인 1인은 불가
// 무조건 한줄 (좌석은 A ~ K, I는 제외 총 10자리)

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

// N = 2 (열 길이)
// S = "1A 2F 1C"
function solution(N, S) {
  seats = Array(N).fill(null).map(() => Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  reserved = S === '' ? null : S.split(" ");
  column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'];
  columnIdx = {}
  for (let i = 0; i < column.length; i++) {
    columnIdx[column[i]] = i;
  }

  // 예약석 표시
  if (reserved) { // 예약좌석 있는 경우만 돌것.
    for (let i = 0; i < reserved.length; i++) {
      seat = reserved[i];
      seatColumn = seat[seat.length - 1];
      seatRow = seat.slice(0, seat.length - 1);
      seats[seatRow - 1][columnIdx[seatColumn]] = 1;
    }
  }

  let count = 0;
  for (let i = 0; i < seats.length; i++) {
    line = seats[i];
    case1 = line.slice(1, 5).includes(1);
    case2 = line.slice(3, 7).includes(1);
    case3 = line.slice(5, 9).includes(1);

    if (!case1) { // 왼쪽 첫번째 경우 가능시
      count += 1;
      if (!case3) { // 거기에 오른쪽 경우 가능 시
        count += 1;
      }
    } else if (!case2) {
      count += 1
    } else if (!case3) {
      count += 1
    }
  }

  return count;
}

console.log(solution(2, "1A 2F 1C"));
console.log(solution(1, ''));

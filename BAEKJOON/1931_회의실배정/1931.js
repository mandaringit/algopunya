const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, schedules) {
  const sortedSchedules = [...schedules]
    .sort((a, b) => a[0] - b[0])
    .sort((a, b) => a[1] - b[1]);
  let meetings = [];
  sortedSchedules.forEach((schedule, i) => {
    if (i === 0) meetings.push(schedule);
    else {
      const recentSchedule = meetings[meetings.length - 1];
      // 최근 스케쥴의 끝나는 시간이 현재 스케쥴의 시작시간보다 작거나 같을때만 푸시
      recentSchedule[1] <= schedule[0] && meetings.push(schedule);
    }
  });
  return meetings.length;
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const N = Number(input[0]);
  const schedules = input.slice(1).map((t) => t.split(' ').map(Number));
  console.log(solution(N, schedules));
  process.exit();
});

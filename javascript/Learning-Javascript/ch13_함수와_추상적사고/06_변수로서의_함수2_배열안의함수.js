// 그래픽 변형의 예
// 시각화 소프트웨어을 만들 때는 변형을 파이프라인으로 묶어서 적용할 때가 많다.

const sin = Math.sin;
const cos = Math.cos;
const theta = Math.PI / 4;
const zoom = 2;
const offset = [1, -3];

const pipeline = [
  function rotate(p) {
    return {
      x: p.x * cos(theta) - p.y * sin(theta),
      y: p.x * sin(theta) + p.y * cos(theta),
    };
  },
  function scale(p) {
    return {x: p.x * zoom, y: p.y * zoom};
  },
  function translate(p) {
    return {x: p.x + offset[0], y: p.y + offset[1]};
  },
];

// pipeline은 2차원 변형에 필요한 함수의 배열이다.
// 점 하나 변형해보기
const p = {x: 1, y: 1};
let p2 = p;
for (let i = 0; i < pipeline.length; i++) {
  p2 = pipeline[i](p2);
}

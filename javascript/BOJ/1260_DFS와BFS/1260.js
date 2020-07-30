const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null;
let M = null;
let V = null;
let i = 0;
const graph = {};

function DFS(x) {
  const stack = [x];
  const visited = [];
  while (stack.length > 0) {
    const node = stack.pop();

    if (!visited.includes(node)) {
      visited.push(node)
      for (let c of [...graph[node]].sort((a, b) => a > b ? -1 : 1)) {
        if (!visited.includes(c)) {
          stack.push(c);
        }
      }
    }
  }
  return visited
}

function BFS(x) {
  const queue = [x];
  const visited = [];

  while (queue.length > 0) {
    const node = queue.shift();
    if (!visited.includes(node)) {
      visited.push(node)
      for (let c of [...graph[node]].sort()) {
        if (!visited.includes(c)) {
          queue.push(c);
        }
      }
    }
  }
  return visited
}

rl.on("line", (line) => {
  if (i === 0) {
    [N, M, V] = line.split(" ").map(Number);
    for (let i = 1; i <= N; i++) {
      graph[i] = [];
    }
  } else {
    const [v1, v2] = line.split(" ").map(Number);
    graph[v1].push(v2)
    graph[v2].push(v1)
  }
  i++
})
  .on("close", () => {
    console.log(DFS(V).join(" "))
    console.log(BFS(V).join(" "))
    process.exit()
  })
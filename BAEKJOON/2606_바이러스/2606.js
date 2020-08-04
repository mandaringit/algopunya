const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let V = null;
let E = null;
const graph = {};
let ln = 0;

function DFS(x) {
  const stack = [x];
  const visited = [x];

  while (stack.length > 0) {
    const node = stack.pop();
    for (let c of graph[node]){
      if(!visited.includes(c)){
        stack.push(c)
        visited.push(c);
      }
    }
  }

  return visited.length -1
}

rl.on("line", (line) => {
  if (ln === 0) {
    V = Number(line);
    for (let i = 1; i <= V; i++) {
      graph[i] = []
    }
  } else if (ln === 1) {
    E = Number(line);
  } else {
    const [v1, v2] = line.split(" ").map(Number);
    graph[v1].push(v2);
    graph[v2].push(v1);
  }
  ln++
})
  .on("close", () => {
    console.log(DFS(1))
    process.exit()
  })
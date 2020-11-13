class MinStack {
  stack: [number, number][];
  constructor() {
    this.stack = [];
  }

  push(x: number): void {
    if (this.stack.length === 0) {
      this.stack.push([x, x]);
    } else {
      const currMin = this.getMin();
      if (currMin > x) {
        this.stack.push([x, x]);
      } else {
        this.stack.push([x, currMin]);
      }
    }
  }

  pop(): void {
    this.stack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1][0];
  }

  getMin(): number {
    return this.stack[this.stack.length - 1][1];
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

export class C {
  static whoAreYou(): string {
    return `I'm class C`;
  }
}

export class D {
  static whoAreYou(): string {
    return `I'm class D`;
  }
}

console.log(C.whoAreYou());
console.log(D.whoAreYou());

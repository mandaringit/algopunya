class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
function oddEvenList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;

  const oddStart = head;
  const evenStart = head.next;

  let oddPointer = oddStart;
  let evenPointer = evenStart;
  head = head.next.next;

  while (head) {
    oddPointer.next = head;
    evenPointer.next = head.next;
    oddPointer = oddPointer.next;
    evenPointer = evenPointer.next;

    head = head.next ? head.next.next : null;
  }

  oddPointer.next = evenStart;

  return oddStart;
}

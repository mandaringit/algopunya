/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function isPalindrome(head: ListNode | null): boolean {
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (slow && fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let node: ListNode | null = null;
  while (slow) {
    const curr = slow;
    const next = slow.next;
    curr.next = node;
    node = curr;
    slow = next;
  }

  while (head && node) {
    if (head.val !== node.val) return false;
    head = head.next;
    node = node.next;
  }

  return true;
}

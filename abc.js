function reverseLinkedList(head) {
  let prev = null;
  let current = head;

  while (current) {
    let nextNode = current.next; // save next
    current.next = prev;         // reverse pointer
    prev = current;              // move prev forward
    current = nextNode;          // move current forward
  }

  return prev; // new head
}

// Build linked list manually: 1 -> 2 -> 3 -> null
let head = { data: 1, next: null };
head.next = { data: 2, next: null };
head.next.next = { data: 3, next: null };

function printList(node) {
  let result = "";
  while (node) {
    result += node.data + " -> ";
    node = node.next;
  }
  console.log(result + "null");
}

console.log("Original:");
printList(head);

let newHead = reverseLinkedList(head);

console.log("Reversed:");
printList(newHead);
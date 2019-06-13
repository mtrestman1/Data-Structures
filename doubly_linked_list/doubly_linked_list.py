"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node

    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1
    

  def remove_from_head(self):
    if self.head == self.tail:
      old_head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return old_head.value

    if self.head is not None: 
      old_head = self.head
      self.delete(self.head)
      return old_head.value
    else:
      return None

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    if self.head == self.tail:
      old_tail = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return old_tail.value

    if self.tail is not None:
      old_tail = self.tail
      self.delete(self.tail)
      return old_tail.value

  def move_to_front(self, node):
    self.delete(node)
    self.add_to_head(node.value)

  def move_to_end(self, node):
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    if self.head == node and self.tail == node:
      self.head = None
      self.tail = None

    if self.head == node:
      self.head = node.next

    if self.tail == node:
      self.tail = node.prev

    self.length -= 1
    return node.value
    
  def get_max(self):
    max_val = 0
    current = self.head
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
    return max_val

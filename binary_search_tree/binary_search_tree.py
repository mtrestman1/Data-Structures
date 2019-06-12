class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif self.left is None and self.right is None:
      return False
    elif target < self.value:
      return self.left.contains(target)
    else:
      return self.right.contains(target)

  def get_max(self):
    pass


  def for_each(self, cb):
    pass
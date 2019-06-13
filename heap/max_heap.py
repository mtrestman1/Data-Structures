class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    if self.storage[0] is True:
      return self.storage[0]
    else:
      False

  def get_size(self):
    pass

  def _bubble_up(self, index):
    if self.storage[index] > self.storage[(index - 1) // 2]:
      self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      self._bubble_up((index - 1) // 2)

  def _sift_down(self, index):
    pass

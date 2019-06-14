class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity 
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print(self.storage)
    if len(self.storage) < self.capacity:
      self.storage.append()
    else:
      self.storage[self.current] =  item
    
    self.current += 1
    if self.current == self.capacity:
        self.current = 0

  def get(self):
    if None in self.storage:
      return self.storage[:self.current]
    else:
      return self.storage
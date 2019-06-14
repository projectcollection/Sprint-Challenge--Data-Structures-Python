class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity 
    self.current = 0
    self.storage = [None]*capacity
    self.none_counter = capacity

  def append(self, item):
    if len(self.storage) < self.capacity:
      self.storage.append()
    else:
      self.storage[self.current] =  item
    
    self.current += 1
    if self.current == self.capacity:
        self.current = 0

    if self.none_counter != 0:
      self.none_counter -= 1

  def get(self):
    if self.none_counter > 0:
      return self.storage[:self.current]
    else:
      return self.storage
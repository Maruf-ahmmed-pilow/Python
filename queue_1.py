class Queue:
    def __init__(self):
        self.item = []
        
        
    def enqueue(self, item):
        self.item.append(item)
        
    def dequeue(self):
        return self.item.pop(0)
            
    def is_empty(self):
        if self.item == []:
            return True
        return False
    
if __name__ == '__main__':
    
        q = Queue()
        q.enqueue = ("Pilow")
        q.enqueue = ('Maruf')
        q.enqueue = ('Ahmmed')
        
        while not q.is_empty():
            person = q.dequeue()
            print(person)
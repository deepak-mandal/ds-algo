  def create_list(self):
        n=int(input('Enter the number of nodes: '))
        if n==0:
            return
        for i in range(n):
            data=int(input('Enter the element to be inserted: '))
            self.insert_at_end(data)
              
    

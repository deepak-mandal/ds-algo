 def insert_in_beginning(self, data):
        temp=node(data)    #allocating the new node
        temp.link=self.start
        self.start=temp
       

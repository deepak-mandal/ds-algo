
    
    def insert_before(self, data, x):
        #if list is empty
        if self.start is None:
            print('list is empty')
            return
        
        #x is in first node, new node is to be inserted before first node
        if x==self.start.info:
            temp=node(data)
            temp.link=self.start
            self.start=temp
            return
        
        #find reference to predecessor of node containing x
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
         
        if p.link is node:
            print(x, 'not present in the list ')
        else:
            temp=node(data)
            temp.link=p.link
            p.link=temp
            
    

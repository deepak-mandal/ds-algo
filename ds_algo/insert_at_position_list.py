
    
    def insert_at_position(self, data, k):
        if k==1:
            temp=node(data)
            temp.link=self.start
            self.start=temp
            return
        
        p=self.start
        i=1
        while i<k-1 and p is not None:    #find a reference to k-1 node
            p=p.link
            i+=1
        if p is None:
            print('You can insert only upto position', i)
        else:
            temp=node(data)
            temp.link=p.link
            p.link=temp
            
    

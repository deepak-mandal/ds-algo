       
    def insert_at_end(self, data):
        temp=node(data)
        if self.start is None:
            self.start=temp
            return
        
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
        
    

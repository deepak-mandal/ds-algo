
    
    def insert_after(self, data, x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        
        if p is None:
            print(x, 'not present in the list')
        else:
            temp=node(data)
            temp.link=p.link
            p.link=temp
            
    

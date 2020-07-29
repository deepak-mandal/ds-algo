        
        
    def insert_cycle(self, x):
        if self.start is None:
            return
        p=self.start
        px=None
        prev=None
        
        while p is not None:
            if p.info==x:
                px=p
            prev=p
            p=p.link
            
        if px is not None:
            prev.link=px
        else:
            print(x, 'not present in list')
            
        
    
  


    
    def delete_node(self, x):
        if self.start is None:
            print('List is empty')
            return
        
        #Deletion of first node
        if self.start.info==x:
            self.start=self.start.link
            return
        
        #Deletion in between or at the end
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        
        if p.link is None:
            print('Element', x, ' not in list ')
        else:
            p.link=p.link.link
            
          

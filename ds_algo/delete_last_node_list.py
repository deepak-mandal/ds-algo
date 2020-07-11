 
    def delete_last_node(self):
        if self.start is None:
            return
        
        if self.start.link is None:
            self.start=None
            return
        
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None
       

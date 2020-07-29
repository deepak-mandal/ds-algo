    
    
    def has_cycle(self):    
        if self.find_cycle() is None:
            return False
        else:
            return True
            
    
    def find_cycle(self):           #detect the cycle in a list using Hare and Tortoise Algorithm
        if self.start is None or self.start.link is None:
            return None
        slowR=self.start
        fastR=self.start
        
        while fastR is not None and fastR.link is not None:
            slowR=slowR.link
            fastR=fastR.link.link
            if slowR==fastR:
                return slowR
        return None        
        
   

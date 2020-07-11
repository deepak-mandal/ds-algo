def search(self, x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print(x, 'is at position ', position)
                return True
            position+=1
            p=p.link
        else:
            print(x, 'not found in the list')
            return False
            
   

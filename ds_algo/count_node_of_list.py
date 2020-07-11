def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.link
        print('Number of nodes in the list = ', n)
    

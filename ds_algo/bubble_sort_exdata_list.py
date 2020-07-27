    
    def bubble_sort_exdata(self):
        end=None
        while end!=self.start.link:
            p=self.start
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.info, q.info=q.info, p.info
                p=p.link
            end=p   
  

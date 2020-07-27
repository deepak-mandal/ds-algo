        
    def bubble_sort_exlinks(self):
        end=None
        while end!=self.start.link:
            r=p=self.start      #r must be before p
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.link=q.link
                    q.link=p
                    if p!=self.start:
                        r.link=q
                    else:
                        self.start=q
                    p, q=q, p
                r=p
                p=p.link
            end=p
            
   

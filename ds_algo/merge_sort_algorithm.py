    
    def merge_sort(self):
        self.start=self._merge_sort_rec(self.start)         #recursive method
    
    def _merge_sort_rec(self, list_start):      #Merge Sort Algorithm
        #if list empty or has one element
        if list_start is None or list_start.link is None:
            return list_start
        #if more than one element
        start1=list_start       #start refs. to 1st node of  the 1st list
        start2=self._divide_list(list_start)         #start2 refs. to 1st node of 2nd list
        start1=self._merge_sort_rec(start1)
        start2=self._merge_sort_rec(start2)
        startM=self._merge2(start1, start2)         #here we merge both by rearranging links
        return startM
    
    
    
    def _divide_list(self, p):
        q=p.link.link
        while q is not None and q.link is not None:
            p=p.link        #p ref. to 1st node of list that has to be divided
            q=q.link.link       #q ref. to 3rd nofe of lidt
        start2=p.link
        p.link=None
        return start2
    
    
        
    def _merge2(self, p1, p2):    #rearranging by links
        if p1.info<=p2.info:
            startM=p1
            p1=p1.link
        else:
            startM=p2
            p2=p2.link
        pM=startM
        
        while p1 is not None and p2 is not None:
            if p1.info<=p2.info:
                pM.link=p1
                pM=pM.link
                p1=p1.link
            else:
                pM.link=p2
                pM=pM.link
                p2=p2.link
                
        if p1 is None:
            pM.link=p2
        else:
            pM.link=p1
        return startM
    

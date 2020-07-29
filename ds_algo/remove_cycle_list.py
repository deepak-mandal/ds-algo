        
    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            return
        print('Node at which the cycle was detected is ', c.info)
        
        p=c
        q=c
        len_cycle=0
        
        while True:
            len_cycle+=1
            q=q.link
            if p==q:
                break
        print('length of cycle is : ', len_cycle)
        
        len_rem_list=0
        p=self.start
        while p!=q:
            len_rem_list+=1
            p=p.link
            q=q.link
        print('Number of nodes not included in the cycle are: ', len_rem_list)
        
        length_list=len_cycle+len_rem_list
        print('length of the list is: ', length_list)
        
        p=self.start        #for removing cycle
        for i in range(length_list-1):
            p=p.link
        p.link=None
        
     

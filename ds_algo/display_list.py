def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print('list is: ')
            p=self.start
            while p is not None:
                print(p.info, ' ', end=' ')
                p=p.link
            print()
       

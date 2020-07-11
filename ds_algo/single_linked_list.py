#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:24:55 2020

@author: deepak
"""


class node:    #---------------------------------------------------------------Class node, that represent node of single linked list
    def __init__(self, value):
        self.info=value
        self.link=None
        
        
class SingleLinkedList:
    def __init__(self):
        self.start=None   
    def display_list(self):
        pass
    def count_nodes(self):
        pass
    def search(self, x):
        pass
    def insert_in_beginning(self, data):
        pass
    def insert_at_end(self, data):
        pass
    def create_list(self):
        pass
    def insert_after(self, data, x):
        pass
    def insert_before(self, data, x):
        pass
    def insert_at_position(self, data, k):
        pass
    def delete_node(self, x):
        pass
    def delete_first_node(self):
        pass
    def delete_firat_node(self):
        pass
    def delete_last_node(self):
        pass
    def reverse_list(self):
        pass
    def bubble_sort_exdata(self):
        pass
    def bubble_sort_exlinks(self):
        pass
    def has_cycle(self):
        pass
    def find_cycle(self):
        pass
    def remove_cycle(self):
        pass
    def insert_cycle(self):
        pass
    def merge2(self, list2):
        pass
    def _merge2(self, p1, p2):
        pass
    def merge_sort(self):
        pass
    def _merge_sort_rec(self, liststart):
        pass
    def divide_list(self, p):
        pass
    
    
    
#------------------------------------------------------------------------------

list=SingleLinkedList()    #---------------------------------------------------Create a new single linked list instance object, 
list.create_list()    #--------------------------------------------------------currently no item in the list because in constructor we have initislze start with none
  
'''
Now inside the while loop will perform various operation on list with the help of all method of single linked list clas;
In this wile loop first we display all the option  then depending on the choice entered we call a particular method of SLL class
'''

while True:
    print('1. Display list')
    print('2. Count the number of the nodes')
    print('3. Search for an elenment')
    print('4. Insert in empty list/Insert in beginning of the list')
    print('5. Insert a node at the end of the list')
    print('6. Insert a node after a specified node')
    print('7. Insert a node before a specified node')
    print('8. Insert a node at a given position')
    print('9. Delete first node')
    print('10. Delete last node')
    print('11. Delete any node')
    print('12. Reverse the list')
    print('13. Bubble sort by exchanging data')
    print('14. Bubble sort by exchanging links')
    print('15. Merge Sort')
    print('16. Insert cycle')
    print('17. Delete cycle')
    print('18. Remove Cycle')
    print('19. Quit')
    
    
    
    option=int(input('Enter your choice: '))
    
    if option==1:
        list.display_list()
        
    elif option==2:
        list.count_nodes()
        
    elif option==3:
        data=int(input('Enter the element to be searched: '))
        list.search(data)
        
    elif option==4:
        data=int(input('Enter the element to be inserted: '))
        list.insert_in_beginning(data)
        
    elif option==5:
        data=int(input('Enter the element to be inserted: '))
        list.insert_at_end(data)
        
    elif option==6:
        data=int(input('Enter the element to be inserted: '))
        x=int(input('Enter the element after which to insert: '))
        list.insert_after(data, x)
       
    elif option==7:
        data=int(input('Enter the element to be inserted: '))
        x=int(input('Enter the element before which to insert: '))
        list.insert_before(data, x)
        
    elif option==8:
        data=int(input('Enter the element to be inserted: '))
        k=int(input('Enter the element position at which to insert: '))
        list.insert_at_position(data, k)
        
    elif option==9:
        list.delete_first_node()
        
    elif option==10:
        list.delete_last_node()
        
    elif option==11:
        data=int(input('Enter the element to be deleted: '))
        list.delete_node(data)
        
    elif option==12:
        list.reverse_list()
        
    elif option==13:
        list.bubble_sort_exdata()
        
    elif option==14:
        list.bubble_sort_exlinks()
        
    elif option==15:
        list.merge_sort()
        
    elif option==16:
        data=int(input('Enter the element at which the cycle has to be inserted: '))
        list.insert_cycle(data)
        
    elif option==17:
        if list.has_cycle():
            print('list has a cycle')
        else:
            print('list doesn\'t have a cycle')
        
    elif option==18:
        list.remove_cycle()
        
    elif option==19:
        break
        
    else:
        print('Wrong option!')
        
    print()
        
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

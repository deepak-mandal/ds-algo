#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:46:06 2020

@author: deepak
"""

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):     #In this constructor, we have EMPTY LIST that will be use to store the element of the stack
        self.items=[]
        
    def is_empty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is Empty')
        return self.items[-1]       #return last element of the list
    
    def display(self):
        print(self.items)
        
############################################################################################
if __name__=='__main__':
    st=Stack()
    
    while True:
        print('1. Push')
        print('2. Pop')
        print('3. Peek')
        print('4. Size')
        print('5. Display')
        print('6. Quit')
        
        choice=int(input('Enter your choice: '))
        
        if choice==1:
            x=int(input('Enter the element to be pushed: '))
            st.push(x)
        elif choice==2:
            x=st.pop()
            print('Popped element is : ', x)
        elif choice==3:
            print('Element at the top is : ', st.peek())
        elif choice==4:
            print('Size of Stack: ', st.size())
        elif choice==5:
            st.display()
        elif choice==6:
            break
        else:
            print('Wrong choice')
        print()
        
    
    
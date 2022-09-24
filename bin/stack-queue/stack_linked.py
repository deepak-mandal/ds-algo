#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:06:14 2020

@author: deepak
"""

class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.info=value
        self.link=None
        
class Stack:
    def __init__(self):
        self.top=None       #top always refers to first node of single linked list & self.top is none mean initially stack is empty
        
    def is_empty(self):
        return self.top==None
    
    def size(self):
        if self.is_empty():
            return 0
        
        count=0
        p=self.top
        while p is not None:
            count+=1
            p=p.link
        return count
    
    
    def push(self, data):
        temp=Node(data)
        temp.link=self.top
        self.top=temp
        
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        
        popped=self.top.info
        self.top=self.top.link
        return popped
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.top.info
    
    def display(self):
        if self.is_empty():
            print('Stack is empty')
            return
        
        print('Stack is: ')
        p=self.top
        while p is not None:
            print(p.info, '')
            p=p.link
            
            
##########################################################################################
if __name__=='__main__':        #here we tested a stack class
    st=Stack()      #creating a new stack object
    
    while True:         #In thiis while loop, we perform various operation
        print('1. push')
        print('2.pop')
        print('3. peek')
        print('4. Size')
        print('5. Display')
        print('6. Quit')
        
        choice=int(input('Enter your choice: '))
        
        if choice==1:
            x=int(input('Enter the element to be pushed: '))
            st.push(x)
        elif choice==2:
            x=st.pop()
            print('popped element is: ', x)
        elif choice==3:
            print('Element at the top is:', st.peek())
        elif choice==4:
            print('size of stack', st.size())
        elif choice==5:
            st.display()
        elif choice==6:
            break
        else:
            print('Wrong choice')
        print()
            
        
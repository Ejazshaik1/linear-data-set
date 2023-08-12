#!/usr/bin/env python
# coding: utf-8

# In[12]:


#q4#
string=str(input("enter a string:"))
num=len(string)
new=str()
for i in range(num):
    a=string[i]
    if a not in new:
        new=new+a
    else:
        break
print(new)


# In[10]:


#q1 list of pairs#
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage
input_array = [2, 4, 3, 5, 6, -2, 8, 7, 1]
target = 6
result = find_pairs_with_sum(input_array, target)

print(f"Pairs with sum {target}: {result}")


# In[13]:


#question-3.
def rotation_string(string1,string2):
    new1=string1[::-1]
    new2=string2[::-1]
    if new1 == new2:
        return "given two strings are rotation of each others"
    return "given two strings are not rotation of each others"
x=input("enter 1st string:")
y=input("enter 1st string:")
rotation_string(x,y)


# In[2]:


#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

array=[]
a=int(input("enter the number of array elements"))
for i in range(a):
    y=input(f"enter {i} element:")
    array.append(y)
print(array)
array=array[::-1]
print("after reversing the array:",array)
        


# In[3]:


#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
  

N = int(input("enter the number:"))
  
TowerOfHanoi(N, 'A', 'C', 'B')
  


# In[ ]:


#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def post_prefix(expression):
    l=len(expression)
    stack=[]
    s=set(['+','-','*','/','=','!','%','<','>'])
    for i in expression:
        if i in s:
            a=stack.pop()
            b=stack.pop()
            t=i+a+b
            stack.append(t)
        else:
            stack.append(i)
    print(stack)
    return 

x=input("enter a postfix expression:")
post_prefix(x)



# In[ ]:


#Q7. Write a program to convert prefix expression to infix expression.
def is_operator(char):
    operators = set(['+', '-', '*', '/', '^'])
    return char in operators

def prefix_to_infix(prefix_expression):
    stack = []
    length = len(prefix_expression)
    
    for i in range(length - 1, -1, -1):
        if not is_operator(prefix_expression[i]):
            stack.append(prefix_expression[i])
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = "(" + operand1 + prefix_expression[i] + operand2 + ")"
            stack.append(infix_expression)
    
    return stack.pop()

prefix_exp = input("enter a expression:")
infix_exp = prefix_to_infix(prefix_exp)
print("Prefix Expression:", prefix_exp)
print("Infix Expression:", infix_exp)


# In[ ]:


#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def bracket_check(string):
    le=len(string)
    stack=[]
    b1,b2,b3,b4,b5,b6=0,0,0,0,0,0
    s=set(['{','}','[',']','(',')'])
    for i in string:
        if i in s:
            b1=b1+1
        elif i in s:
            b2=b2+1
        elif i in s:
            b3=b3+1
        elif i in s:
            b4=b4+1
        elif i in s:
            b5=b5+1
        elif i in s:
            b6=b6+1
    if b1==b2:
        if b3==b4:
            if b5==b6:
                print("all brackets are closed.")
            else:
                print("() are open.")
        else:
            print("[] are open.")
    else:
        print("{} are open.")

x=input("enter a expression:")
bracket_check(x)


# In[ ]:


#Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

# Example usage
original_stack = Stack()
original_stack.push(1)
original_stack.push(2)
original_stack.push(3)
original_stack.push(4)

print("Original Stack:", original_stack.items)

reverse_stack(original_stack)

print("Reversed Stack:", original_stack.items)

        


# In[ ]:


#Q10. Write a program to find the smallest number using a stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # This stack will track the minimum values

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = MinStack()
stack.push(4)
stack.push(2)
stack.push(6)
stack.push(1)

print("Smallest number in the stack:", stack.get_min())

stack.pop()
stack.pop()

print("Smallest number in the stack after pops:", stack.get_min())

            
        


# In[ ]:





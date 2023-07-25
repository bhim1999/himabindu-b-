2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
  
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\reverse_array.py"
[1, 2, 3, 4, 5, 6]
Reversed list is  
[6, 5, 4, 3, 2, 1]

3.Write a program to check if two strings are a rotation of each other?

def check_rotation(s, goal):
 
    if (len(s) != len(goal)):
        skip
 
    q1 = []
    for i in range(len(s)):
        q1.insert(0, s[i])
 
    q2 = []
    for i in range(len(goal)):
        q2.insert(0, goal[i])
 
    k = len(goal)
    while (k > 0):
        ch = q2[0]
        q2.pop(0)
        q2.append(ch)
        if (q2 == q1):
            return True
 
        k -= 1
 
    return False
 
 
# Driver code
if __name__ == "__main__":
 
    string1 = "AACD"
    string2 = "ACDA"
 
    # Function call
    if check_rotation(string1, string2):
        print("two Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")
 
output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\two-strings.py"
two Strings are rotations of each other

4.Write a program to print the first non-repeated character from a string?

string = "hihello"
index = -1
fnc = ""
 
if len(string) == 0 :
  print("EMTPY STRING");
 
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\non_repeating.py"
First non-repeating character is i

Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
  
# Driver code
N = 3
  
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\hongi_algaritham.py"
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C

Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
    # length of expression
    length = len(post_exp)
 
    # reading from right to left
    for i in range(length):
 
        # check if symbol is operator
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            s.append(temp)
 
      
        else:
 
            
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\prefix_postfix.py"
Prefix :  +AB-CD

Q7. Write a program to convert prefix expression to infix expression.

# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
	stack = []
	
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
		else:
		
			# symbol is operator
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
	str = "*-A/BC-/him"
	print(prefixToInfix(str))
	

output:

PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\prefix_infix.py"
((A-(B/C))*((h/i)-m))

Q8. Write a program to check if all the brackets are closed in a given code snippet.

# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\balanced_brakets.py"
Balanced

Q9. Write a program to reverse a stack.

# Python program to reverse a
# stack using recursion

# Below is a recursive function
# that inserts an element
# at the bottom of a stack.


def insertAtBottom(stack, item):
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)

# Below is the function that
# reverses the given stack
# using insertAtBottom()


def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

# Below is a complete running
# program for testing above
# functions.

# Function to create a stack.
# It initializes size of stack
# as 0


def createStack():
	stack = []
	return stack

# Function to check if
# the stack is empty


def isEmpty(stack):
	return len(stack) == 0

# Function to push an
# item to stack


def push(stack, item):
	stack.append(item)

# Function to pop an
# item from stack


def pop(stack):

	# If stack is empty
	# then error
	if(isEmpty(stack)):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack


def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end=' ')
	print()

# Driver Code


stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)

reverse(stack)

print("Reversed Stack ")
prints(stack)

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\reverse_stack.py"
Original Stack 
1 2 3 4
Reversed Stack
4 3 2 1

Q10. Write a program to find the smallest number using a stack.

# Python program for the above approach
class MinStack:

	# initialize your data structure here.
	def __init__(self):
		self.s = []

	class Node:
		def __init__(self, val, Min):
			self.val = val
			self.min = Min

	def push(self, x):
		if not self.s:
			self.s.append(self.Node(x, x))
		else:
			Min = min(self.s[-1].min, x)
			self.s.append(self.Node(x, Min))

	def pop(self):
		return self.s.pop().val

	def top(self):
		return self.s[-1].val

	def getMin(self):
		return self.s[-1].min

s = MinStack()

# Function calls
s.push(-1)
s.push(10)
s.push(-4)
s.push(0)
print(s.getMin())
print(s.pop())
print(s.pop())
print(s.getMin())


output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\smallest_stack.py"
-4
0
-4
-1

1Q.Implement Binary tree

# Binary Tree in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\binary_tree.py"
Pre order Traversal: 1 2 4 3  
In order Traversal: 4 2 1 3   
Post order Traversal: 4 2 3 1 

2Q.Find height of a given tree

# Python3 program to find the maximum depth of tree

# A binary tree node


class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
	if node is None:
		return 0

	else:

		# Compute the depth of each subtree
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)

		# Use the larger one
		if (lDepth > rDepth):
			return lDepth+1
		else:
			return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Height of tree is %d" % (maxDepth(root)))

# This code is contributed by Amit Srivastav
OUTPUT:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\HEIGHT.PY"
Height of tree is 3

3Q.Perform Pre-order, Post-order, In-order traversal

# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Inorder traversal of binary tree is:")
	printInorder(root)
# Python3 program to for tree traversals


# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val, end=" "),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Preorder traversal of binary tree is:")
	printPreorder(root)

# Python3 program to for tree traversals


# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# The recur on right child
		printPostorder(root.right)

		# Now print the data of node
		print(root.val, end=" "),


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Postorder traversal of binary tree is:")
	printPostorder(root)
OUTPUT:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\TRAVERSAL.PY"
Inorder traversal of binary tree is:
4 2 5 1 3 Preorder traversal of binary tree is:
1 2 4 5 3 Postorder traversal of binary tree is:
4 5 2 3 1

4Q.Function to print all the leaves in a given binary tree

# Python3 program to print
# leaf nodes from left to right

# Binary tree node
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to print leaf
# nodes from left to right
def printLeafNodes(root: Node) -> None:

	# If node is null, return
	if (not root):
		return

	# If node is leaf node,
	# print its data
	if (not root.left and
		not root.right):
		print(root.data,
			end = " ")
		return

	# If left child exists,
	# check for leaf recursively
	if root.left:
		printLeafNodes(root.left)

	# If right child exists,
	# check for leaf recursively
	if root.right:
		printLeafNodes(root.right)

# Driver Code
if __name__ == "__main__":

	# Let us create binary tree shown in
	# above diagram
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(8)
	root.right.left.left = Node(6)
	root.right.left.right = Node(7)
	root.right.right.left = Node(9)
	root.right.right.right = Node(10)

	# print leaf nodes of the given tree
	printLeafNodes(root)

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\leaves.py"
4 6 7 9 10 

5Q.Implement BFS (Breath First Search) and DFS (Depth First Search)
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Breadth First Traversal:")
	g.BFS(2)

# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	
	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	
	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)


# Driver's code
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Depth First Traversal:")
	
	# Function call
	g.DFS(2)
output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\bfs_dfs.py"
Breadth First Traversal:
2 0 3 1 Depth First Traversal:
2 0 1 3

6Q.Find sum of all left leaves in a given Binary Tree

# Python program to find sum of all left leaves

# A Binary tree node
class Node:
	# Constructor to create a new Node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to check if a given node is leaf or not
def isLeaf(node):
	if node is None:
		return False
	if node.left is None and node.right is None:
		return True
	return False

# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):

	# Initialize result
	res = 0
	
	# Update result if root is not None
	if root is not None:

		# If left of root is None, then add key of
		# left child
		if isLeaf(root.left):
			res += root.left.key
		else:
			# Else recur for left child of root
			res += leftLeavesSum(root.left)

		# Recur for right child of root and update res
		res += leftLeavesSum(root.right)
	return res

# Driver program to test above function

# Let us construct the Binary Tree shown in the above function
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)	
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\left_leaves.py"
Sum of left leaves is 78

7Q.Find sum of all nodes of the given perfect binary tree
# Python3 program to implement the
# above approach

# function to find Sum of all of the
# nodes of given perfect binary tree
def SumNodes(l):
	
	# no of leaf nodes
	leafNodeCount = pow(2, l - 1)

	# list of vector to store nodes of
	# all of the levels
	vec = [[] for i in range(l)]

	# store the nodes of last level
	# i.e., the leaf nodes
	for i in range(1, leafNodeCount + 1):
		vec[l - 1].append(i)

	# store nodes of rest of the level
	# by moving in bottom-up manner
	for i in range(l - 2, -1, -1):
		k = 0

		# loop to calculate values of parent nodes
		# from the children nodes of lower level
		while (k < len(vec[i + 1]) - 1):

			# store the value of parent node as
			# Sum of children nodes
			vec[i].append(vec[i + 1][k] +
						vec[i + 1][k + 1])
			k += 2

	Sum = 0

	# traverse the list of vector
	# and calculate the Sum
	for i in range(l):
		for j in range(len(vec[i])):
			Sum += vec[i][j]

	return Sum

# Driver Code
if __name__ == '__main__':
	l = 3

	print(SumNodes(l))
	

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\sum_nodes_perfectBT.py"
30

8Q.Count subtress that sum up to a given value x in a binary tree
# Python3 implementation to count subtrees
# that Sum up to a given value x

# class to get a new node


class getNode:
	def __init__(self, data):

		# put in the data
		self.data = data
		self.left = self.right = None

# function to count subtrees that
# Sum up to a given value x


def countSubtreesWithSumX(root, count, x):

	# if tree is empty
	if (not root):
		return 0

	# Sum of nodes in the left subtree
	ls = countSubtreesWithSumX(root.left,
							count, x)

	# Sum of nodes in the right subtree
	rs = countSubtreesWithSumX(root.right,
							count, x)

	# Sum of nodes in the subtree
	# rooted with 'root.data'
	Sum = ls + rs + root.data

	# if true
	if (Sum == x):
		count[0] += 1

	# return subtree's nodes Sum
	return Sum

# utility function to count subtrees
# that Sum up to a given value x


def countSubtreesWithSumXUtil(root, x):

	# if tree is empty
	if (not root):
		return 0

	count = [0]

	# Sum of nodes in the left subtree
	ls = countSubtreesWithSumX(root.left,
							count, x)

	# Sum of nodes in the right subtree
	rs = countSubtreesWithSumX(root.right,
							count, x)

	# if tree's nodes Sum == x
	if ((ls + rs + root.data) == x):
		count[0] += 1

	# required count of subtrees
	return count[0]


# Driver Code
if __name__ == '__main__':

	# binary tree creation
	#		 5
	#		 / \
	#	 -10	 3
	#	 / \ / \
	#	 9 8 -4 7
	root = getNode(5)
	root.left = getNode(-10)
	root.right = getNode(3)
	root.left.left = getNode(9)
	root.left.right = getNode(8)
	root.right.left = getNode(-4)
	root.right.right = getNode(7)

	x = 7

	print("Count =",
		countSubtreesWithSumXUtil(root, x))


output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\count_subtree.py"
Count = 2

9Q.Find maximum level sum in Binary Tree
# A queue based Python3 program to find
# maximum sum of a level in Binary Tree
from collections import deque

# A binary tree node has data, pointer
# to left child and a pointer to right
# child
class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

# Function to find the maximum sum
# of a level in tree
# using level order traversal
def maxLevelSum(root):
	
	# Base case
	if (root == None):
		return 0

	# Initialize result
	result = root.data
	
	# Do Level order traversal keeping
	# track of number
	# of nodes at every level.
	q = deque()
	q.append(root)
	
	while (len(q) > 0):
		
		# Get the size of queue when the
		# level order traversal for one
		# level finishes
		count = len(q)

		# Iterate for all the nodes in
		# the queue currently
		sum = 0
		while (count > 0):
			
			# Dequeue an node from queue
			temp = q.popleft()

			# Add this node's value to current sum.
			sum = sum + temp.data

			# Enqueue left and right children of
			# dequeued node
			if (temp.left != None):
				q.append(temp.left)
			if (temp.right != None):
				q.append(temp.right)
				
			count -= 1

		# Update the maximum node count value
		result = max(sum, result)

	return result
	
# Driver code
if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(8)
	root.right.right.left = Node(6)
	root.right.right.right = Node(7)

	# Constructed Binary tree is:
	#			 1
	#		 / \
	#		 2	 3
	#	 / \	 \
	#	 4 5	 8
	#				 / \
	#			 6	 7
	print("Maximum level sum is", maxLevelSum(root))


output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\sum_BT"
Maximum level sum is 17

10Q.Print the nodes at odd levels of a tree

# Recursive Python3 program to print
# odd level nodes

# Utility method to create a node
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def printOddNodes(root, isOdd = True):
	
	# If empty tree
	if (root == None):
		return

	# If current node is of odd level
	if (isOdd):
		print(root.data, end = " ")

	# Recur for children with isOdd
	# switched.
	printOddNodes(root.left, not isOdd)
	printOddNodes(root.right, not isOdd)

# Driver code
if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	printOddNodes(root)
	

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\odd_levels.py"
1 4 5 


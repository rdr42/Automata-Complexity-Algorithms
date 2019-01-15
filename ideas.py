
alphabet = {0,1,2,3,4,5,6,7,8,9,'+','*','(',')'}
alphabet_num = {0,1,3,4,5,6,7,8,9}
alphabet_op = {'+','*'}
alphabet_or = {'(',')'}
var = "(( 3 + 2 ) * 6 ) * ( 6 + 9 )"

new_var = var.split()

class Tree(object):
    def __init__(self):
        self.child = []
        self.root = None
        self.tree = []
        
        
    def children(self,element):
      self.child.append(element)
    
    def parent(self,element):
      self.root = element
      
    def get_node(self):
      el = {self.root:self.child}
      self.root = []
      self.child = []
      return el
      
#Some ideas on how the program could work... I forgot what we talked about in class regarding
#the recursion

   
class Node(object):
  def __init__(self):
    self.node = []
    self.root = None                       



x = Tree()
y = Node()



for i in range(len(new_var)):
  if new_var[i] == '(':
    x.children(new_var[i+1])
  
  if new_var[i] == ')':
    x.children(new_var[i-1])
    y.node.append(x.get_node())

  if new_var[i] == '*' or new_var[i] == '+':
    if i + 1 < len(new_var):
      if new_var[i-1] == ')' :
        y.root = new_var[i]
    if i - 1 >= 0:
      if new_var[i+1] == '(' :
        y.root = new_var[i]
   

  if new_var[i] == '*' or new_var[i] == '+':
    x.parent(new_var[i])
print(y.root)
print(y.node)

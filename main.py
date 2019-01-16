import ast
import operator

alphabet_num = {0,1,2,3,4,5,6,7,8,9}
alphabet_op = {'+','*'}
alphabet_od = {'(',')',' '}

OPERATORS = {ast.Add : operator.add,
             ast.Mult : operator.mul}

 #OPERATOR = {'+' : operator.add,
 #           '*' : operator.mul}

#Take the input as a string
var = input()
parsed_var = ' '.join(var.split())
parsed_var = parsed_var.split(' ');



  #Exceptions:
    #Missing parantheses
    #Numbers separated by space
    #Operators followed by operators

  #How to solve the calculation:
    #Depth Counter to solve inner most operation
    #Recursion to solve 
  
  #return value or exception


class str_calc(ast.NodeVisitor):

    def visit_op(self, node):
        left_side = self.visit(node.left_side)
        right_side = self.visit(node.right_side)
        return OPERATORS[type(node.op)](left_side, right_side)

    def visit_exp(self, node):
        return self.visit(node.value)

    def visit_number(self, node):
        return node.n

    @classmethod
    def eval_expr(cls, expr):
        tree = ast.parse(expr)
        print (ast.dump(tree.body[0]))
        calculating = cls()
        return calculating.visit(tree.body[0])

print (str_calc.eval_expr(var))

#Calling function to execute program
#parsing(var)

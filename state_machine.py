degree = {'(',')','*', '+'}

#Slice array and solve equation
def solve(piece):
  if piece[1] == '+':
    val = int(piece[0]) + int(piece[2])
    val = str(val)
    return val
  if piece[1] == '*':
    val = int(piece[0]) * int(piece[2])
    val = str(val)
    return val


#Function contains two states
#With parentheses and without parentheses
def evaluate(var):
  stateA = 1
  stateB = 0

  p_counter = 0
  result = False  
  iterations = 0
  while result != True:
    
    for j in range(len(var)):
    
      if len(var) == 1:
        result = True
        break
      
      if stateA == 1:
        if var[j] == ')':
          chunk = var[j-3:j]
          chunk = solve(chunk)
          if len(var) == 5:
              var = chunk
              result = True
          else:
              v = var[:j-4]
              v.append(chunk)
              v.extend(var[j+1:])
              var = v
              stateB = 1
              stateA = 0
          break
        else:
            if ')' not in var:
                stateB = 1
                stateA = 00
      
      if stateB == 1:
        for i in var:
            if i == ')':
                stateB = 0
                stateA = 1
                break
        if var[j] == '*' or var[j] == '+':
          chunk = var[j-1:j+2]
          chunk = solve(chunk)

          if len(var) == 3:
            var = chunk
            result = True
          else:
            
            var[j-1:j+2] = chunk
            
          break
  
  print(var) #printing result
vd = input()
vd = vd.split()

evaluate(vd)

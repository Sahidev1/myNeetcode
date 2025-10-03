

class Stack:
    def __init__(self):
        self.array = []
        
    def push(self, E):
        self.array.append(E)
        
    def pop(self):
        return self.array.pop()
    

class Solution:
    
    def isNum(self, tok:str):
        if len(tok) > 1 and tok[0] == '-' and tok[1:].isdigit(): return True
        elif tok.isdigit(): return True
        return False
    
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack: Stack[str] = Stack()
        
        for tok in tokens:
            if self.isNum(tok) :
                stack.push(tok)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                
                res=0
                match tok:
                    case "+":
                        res = left + right
                    case "-": 
                        res = left - right
                    case "*":
                        res = left*right
                    case "/":
                        res = int(left/right)
                    case _:
                        raise Exception("nahh")
                
                stack.push(str(res))
                
        
        #print(stack.array)         
        
        return int(stack.pop())
    
    

sol = Solution()

tokens = ["2","1","+","3","*"]
##print(tokens)
res = sol.evalRPN(tokens)
#print(res)
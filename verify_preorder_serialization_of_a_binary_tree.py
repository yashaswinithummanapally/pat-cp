class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        lst=[node for node in preorder.split(',')]
        stack=[]
        if(len(lst)<3):
            if(len(lst)==1 and lst[0]=='#'):
                return True
            else:
                return False
        else:
            j=0
            for node in lst:
                if(node!='#'):
                    stack.append(node)
                else:
                    if(len(stack)==0):
                        if(len(lst)==j+1):
                            return True
                        else:
                            return False
                    else:
                        stack.pop()
                j+=1
            else:
                if(len(stack)>0):
                    return False
                else:
                    return True
class stack:
    def __init__(self):
        self.mylist=[]
    def isempty(self):
        return len(self.mylist)==0
    def push(self,val):
        self.mylist.append(val)
    def pop(self):
        return self.mylist.pop()
    def peek(self):
        return self.mylist[-1]
def getParenthesis(ch):
    match ch:
        case ')':
            return '('
        case '}':
            return '{'
        case ']':
            return '['
def cp(src):
    st=stack()
    for ch in src:
        if ch in '({[':
            st.push(ch)
        elif ch in ')}]':
            if st.isempty() or getParenthesis(ch)!=st.pop():
                print("Error")
                return False
    if st.isempty():
        return True
    else:
        return False
source=input("Enter any arithmetic expression: ")
result=cp(source)
if result is True:
    print("Parenthesis are well placed")
else:
    print("Parenthesis are not well placed")
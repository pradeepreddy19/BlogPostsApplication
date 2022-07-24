# inp= "5 1 2 + 4 * + 3 -"

# def postfix(data):
#     post_fix_data = data.split(" ")

#     if len(post_fix_data)==0:
#         return -1

#     stack=[]

#     for each in post_fix_data:
#         if each in ["+","-","/","*"]:
#             a=stack.pop()
#             b=stack.pop()
#             stack.append(eval(b+each+a))
#         else:
#             stack.append(each)
            
#     return stack[0]

# print(postfix(inp))

# def valid_parenthesis(inp):
#     stack=[]
#     pd={")":"(","}":"{","]":"["}
#     if len(inp)<=1:
#         return False
#     for each in inp:
#         if each in pd.values():
#             stack.append(each)
#         else:
#             if stack:
#                 if stack.pop()!=pd[each]:
#                     return False
#             else:
#                 return False
    
#     return True if len(stack)==0 else False

# inp1="(){}[]"
# print(valid_parenthesis(inp1))
# inp2="()()((())"
# print(valid_parenthesis(inp2))
# inp3="}"
# print(valid_parenthesis(inp3))
# inp3="{}{{}}{}{}"
# print(valid_parenthesis(inp3))
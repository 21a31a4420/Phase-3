# def find(nums):
#     n=len(nums)
#     stack=[]
#     res=[-1]*n
#     for idx in range(n-1,-1,-1):
#         # step1(remove unnecessary values)
#         while len(stack)>0:
#             if stack[-1]<=nums[idx]:
#                 stack.pop()
#             else:
#                 break
#         if len(stack)>0:
#             res[idx] =stack[-1]
#         stack.push(nums[idx])
#     return res
# # nums=[4,6,2,8,3,10]
# print(find(nums))


    
# nums=[73,74,75,71,69,72,76,73]

# preorder traversal iteratice approach using stacks
def preorderTraversal(self, root):
        if root == None:
            return []
            
        result = []
        stack = [[root, 1]]
        while len(stack) > 0:
            curr = stack[-1]
            if curr[1] == 1:
                result.append(curr[0].val)
                curr[1] += 1  
                if curr[0].left:
                    stack.append([curr[0].left, 1])
            elif curr[1] == 2:
                # result.append(curr[0].val)
                curr[1] += 1 
                if curr[0].right:
                    stack.append([curr[0].right, 1])
            else:
                #result.append(curr[0].val)
                stack.pop()
        return result
nums =[1,2,3,4,5]
print(preorderTraversal(nums,[1]))


# 1.Pre-order,Inorder,post-order (Both Recursive and Iterative)
# 1.Level order Traversal of BinaryTree
# 2.Zigzag order traversal of binary tree
# 3.Max Level sum of a BT
# 4.Left view of BT
# 5.Right view of BT
# 6.Top view of BT
# 7.Bottom view of BT
# 8.Boundary Traversal of BT

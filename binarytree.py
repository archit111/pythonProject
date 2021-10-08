
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def printLeafNode(root:Node):

    if (root is None):
        return

    if (root.left is None  and root.right is None ):
        print (root.data)
    if root.left:
        printLeafNode(root.left)
    if root.right :
        printLeafNode(root.right)

def InorderTraversal(root:Node):

    if(root is None ):
        return
    else:

        InorderTraversal(root.left)
        print(root.data)
        InorderTraversal(root.right)

def PreorderTraversal(root:Node):

    if(root is None ):
        return
    else:
        print(root.data)
        PreorderTraversal(root.left)
        PreorderTraversal(root.right)

def PostorderTraversal(root:Node):

    if(root is None ):
        return
    else:
        PostorderTraversal(root.left)
        PostorderTraversal(root.right)
        print(root.data)

def breadthfirstsearch(root:Node):
    queue=[]
    temp=0
    queue.append(root)

    while(len(queue)>0):
        print(queue[0].data)
        temp=queue.pop(0)

        if (temp.left):
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)



def height(root:Node):
    if (root is None):
        return 0
    # compute the height of each subtree
    lheight=height(root.left)
    rheight=height(root.right)
    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1

def insertion (temp,key):
    if not temp:
        root=Node(key)
        return
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if temp.left is None:
            temp.left =Node(key)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

def size(root):
    if root is None :
        return 0
    else:
        return (size(root.left)+size(root.right)+1)

def maximum(root):
     if root is None:
         return 0
     r=root.data
     lroot=maximum(root.left)
     rroot=maximum(root.right)
     if lroot> r:
         r=lroot
     if rroot>r:
         r=rroot
     return r

def minimum(root):
     if root is None:
         return 0
     r=root.data
     lroot=minimum(root.left)
     rroot=minimum(root.right)
     if lroot<r:
         r=lroot
     if rroot<r:
         r=rroot
     return r
def printleafnodes(root):
    if root.left is None and root.right is None :
        print(root.data)
    if root.left!=None:
        printleafnodes(root.left)

    if root.right!=None:
        printleafnodes(root.right)

'''def min(root):

    if root.left==None:
        print (root.data)
    if root.left!=None:
        min(root.left)'''
def depth(root):
    if root is None:
        return 0
    ldepth=depth(root.left)
    rdepth=depth(root.right)
    if ldepth>rdepth:
        return ldepth+1
    else:
        return rdepth+1
def leftviewUtil(root,level,max_level):
    if root is None :
        return 0

    if (max_level[0]<level):
        print(root.data,end=" ")
        max_level[0]=level

    leftviewUtil(root.left,level+1,max_level)
    leftviewUtil(root.right,level+1,max_level)

def leftview(root):
    max_level=[0]
    level=1
    leftviewUtil(root,level,max_level)


def rightviewUtil(root,level,max_level):
    if root is None:
        return 0

    if (max_level[0]<level):
        print(root.data,end=" ")
        max_level[0]=level

    rightviewUtil(root.right,level+1,max_level)
    rightviewUtil(root.left,level+1,max_level)


def rightview(root):
    level=1
    max_level=[0]
    rightviewUtil(root,level,max_level)

def topviewUtil(root,level,max_level):
    if root is None:
        return 0

    if (max_level[0]<level):
        print(root.data,end=" ")
        max_level[0]=max_level[0]+1

    topviewUtil(root.left,level+2,max_level)
    topviewUtil(root.right,level+2,max_level)


'''def spiralview(root):
       if root.left is not None and root.right is not None :
        spiralview(root.right)
        spiralview(root.left)
        print (root.data)

    if root.left is None and root.right is None :
        print (root.data)
    spiralview(root.right )
    spiralview(root.left)'''

def sumofnodes(root):
    if root is None :
        return 0
    return root.data+sumofnodes(root.left) +sumofnodes(root.right )

def sumofparentnodestwochildnodes(root):
    if root.left is None or root.right is None:
        return 0
    return root.data +sumofparentnodestwochildnodes(root.left)+sumofparentnodestwochildnodes(root.right )

def isleaf(root):
    if root is None :
        return False
    if root.left is None and root.right is None :
        return True
    return False

def sumofallleftleaves(root):
    c=0
    if root is not None:
        if isleaf(root.left):
            c = c + root.left.data
        else:
            c = c + sumofallleftleaves(root.left)
            c=c+sumofallleftleaves(root.right)
    return c

def sumofallrightleaves(root):
    c=0
    if root is not None:
        if isleaf(root.right):
            c=c+root.right.data
        else:
            c=c+sumofallrightleaves(root.right)
            c=c+sumofallrightleaves(root.left)
    return c

def printnodesatoddlevel(root):
    if root is None:
        return
    q=[]
    q.append(root)
    isroot = True
    while(1):


        countnodes=len(q)
        if countnodes==0:
            break
        while (countnodes>0):
            root=q[0]
            if (isroot):
                print(root.data,end=" ")
            q.pop(0)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
            countnodes -= 1

        isroot=not(isroot)


def printpathfromroottonode(root,arr,n):
    if root is None :
        return False
    arr.append(root)

    if root.data==n:
        return True
    if printpathfromroottonode(root.left,arr,n)or printpathfromroottonode(root.right,arr,n):
        return True
    arr.pop(-1)

    return False



def printPath(root, x):
    # vector to store the path
    arr = []

    # if required node 'x' is present
    # then print the path
    if (printpathfromroottonode(root, arr, x)):
        for i in range(len(arr)):
            print(arr[i].data, end="->")


        # 'x' is not present in the
    # binary tree
    else:
        print("No Path")

'''def longestleafpath(root):
    if root is None :
        return 0
    
    leftvector=longestleafpath(root.left)
    rightvector=longestleafpath(root.right)

    if len(leftvector)> len(rightvector):
        leftvector.append(root)
    else:
        rightvector.append(root)
    return leftvector'''

def printfullnodes(root):
    if root is None :
        return 0
    if root.left !=None and root.right !=None:
        print(root.data)
    printfullnodes(root.left)
    printfullnodes(root.right)

def roottoleafpath(root,arr,arrLen):
    if root is None:
        return 0
    if len(arr)>arrLen:
        arr[arrLen]=root.data
    else:
        arr.append(root.data)
    arrLen=arrLen+1
    if root.left is None or root.right is None :
        return True
    roottoleafpath(root.left,arr,arrLen)
    roottoleafpath(root.right,arr,arrLen)
    return  arr


def printroottoleafpath(root):
    arr=[]
    if (roottoleafpath(root,arr,0)):
        for i in range (0,len(arr)):
            print(arr[i],end="-> ")


def mirror(root):
    if root is None :
        return 0
    else:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left

def ancestors(root,target_node):
   if root == None :
       return 0
   if root.data==target_node:
       #print(root.data)
       return 1
   if(ancestors(root.left,target_node) or ancestors(root.right,target_node)):
       print(root.data)
       return 1

def kthmaxvalue(root):
    li=[]
    li.append(root.data)
    if root ==None :
        return 0
    if len(li)!=size(root):
        if root.left:
            li.append(root.left.data)
        if root.right:
            li.append(root.right.data)

    li.sort(reverse=True)
    return li

def kthdistance (root,K):
    if root ==None :
        return 0

    if K==0:
        print (root.data,end=" ")
    kthdistance(root.left,K-1)
    kthdistance(root.right,K-1)

def zigzagorder(root):
    queue=[]
    nextlevel=[]
    ltr=True

    if root ==None :
        return 0

    queue.append(root)
    while (len(queue)>0):
        temp=queue.pop(-1)
        print (temp.data," ",end=" ")

        if ltr:
            if (temp.left):
                nextlevel.append(temp.left)
            if (temp.right):
                nextlevel.append(temp.right)

        else:
            if (temp.right):
                nextlevel.append(temp.right)
            if (temp.left):
                nextlevel.append(temp.left)

        if len(queue)==0:
            ltr=not(ltr)
            queue,nextlevel=nextlevel,queue

def childrensumproperty(root):
    sum=0
    if root ==None:
        return True
    if root.left==None and root.right==None :
        return True
    if root.left!=None :
        sum+=root.left.data
    if root.right!=None :
        sum+=root.right.data
    if (sum==root.data and childrensumproperty(root.left) and childrensumproperty(root.right)):
        return True
    else:
        return False


def maximum(root):

    if root==None :
        return 0
    return max(root.data,max(maximum(root.left),maximum(root.right)))


def findpath(root,p,n):
    if root==None :
        return False
    p.append(root.data)
    if (root.data==n):
        return True
    if (findpath(root.left,p,n) or findpath(root.right,p,n)):
        return True
    p.pop()
    return False

def lowestcommonancestor (root,n1,n2):
    if root==None :
        return 0
    path1=[]
    path2=[]
    if (findpath(root,path1,n1)==False or findpath(root,path2,n2)==False):
        return False
    i=0
    while (i<len(path1) and i<len(path2)):
        if (path1[i]!=path2[i]):
            break
        i=i+1
    return path1[i-1]



def balanceTree(root):
    if root==None :
        return
    height_l=height(root.left)
    height_r=height(root.right)
    if (height_l-height_r<=1 ):
        return True
    else:
        return False




if __name__=="__main__":

    '''root=Node(6)
    root.left=Node(4)
    root.right=Node(9)
    root.left.left=Node(3)
    root.right.right=Node(10)
    root.right.left=Node(7)
    root.left.right=Node(5)
    root.right.left.left=Node(9)'''
    root=Node(10)
    root.left=Node(8)
    root.right=Node(2)
    root.left.left=Node(3)
    root.left.right=Node(5)
    root.left.right.left=Node(15)
    root.right.left=Node(7)
    #printLeafNode(root)
    #InorderTraversal(root)
    #PreorderTraversal(root)
    #PostorderTraversal(root)
    #breadthfirstsearch(root)
    #maxheight(root)
    #print(height(root))
    #insertion(root,5)
    #deletion(root,2)
    #print(size(root))
    #print(maximum(root))
    #print (minimum(root))
    #printleafnodes(root)
    #leftview(root)
    #rightview(root)
    #print (sumofnodes(root))
    #print(sumofparentnodestwochildnodes(root))
    #print (sumofallleftleaves(root))
    #print (sumofallrightleaves(root))
    #printnodesatoddlevel(root)
    #printPath(root,5)
    #printfullnodes(root)
    #printroottoleafpath(root)
    #mirror(root)
    #InorderTraversal(root)
    #ancestors(root,3)
    #print(kthmaxvalue(root))
    #kthdistance(root,1)
    #zigzagorder(root)
    #print(childrensumproperty(root))
    #print (maximum(root))
    #print(lowestcommonancestor(root,2,8))
    print(balanceTree(root))
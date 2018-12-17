m = int(input("请输入墙面的长："))
n = int(input("请输入墙面的宽："))
a = int(input("请输入瓷砖的长："))
b = int(input("请输入瓷砖的宽："))
numbers = int((m*n)/(a*b))
qiang = [[0]*m]*n #假设墙是一个二维列表，qiang[i][j]表示第i行第j列的墙上方块的状态，1表示被铺了，0表示没被铺。
ans = []

def puzhuan(ans):
    hang = 0
    lie = 0
    newbrick = []
    for i in range(n): 
        for j in range(m):
            if qiang[i][j] == 0:
                hang = i
                break
        lie = j
        break #遍历qiang，找到下一个没被铺的方块位置，行号i，列号为j

    if hang == n-1 and lie == m-1: #不存在下一个没被铺的方块（说明铺满了）
        return ans #记录ans，即记录这次搜索出的铺法。终止递归，直接返回

    if (hang + b) <= n and (lie + a) <= m: #从(i,j)开始能横着铺
        for h in range(b):
            for l in range(a):
                qiang[hang+h][lie+l] = 1 #从(i,j)开始改变qiang相应的位置状态，铺上横着铺的瓷砖
        for zhuandehang in range(b):
            for zhuandelie in range(a):
                newbrick.append(hang + zhuandelie + a * zhuandehang) #ans中加入该瓷砖铺好的方块编号
        ans.append(tuple(newbrick))
        puzhuan(ans) #递归调用铺下一个
        for h in range(b):
            for l in range(a):
                qiang[hang+h][lie+l] = 0 #从(i,j)开始改变qiang相应的位置状态，拆下横着铺的瓷砖
        ans.pop() #ans中去除该瓷砖铺好的方块编号 

    if (hang + a) <= n and (lie + b) <= m: #从(i,j)开始能竖着铺
        for h in range(a):
            for l in range(b):
                qiang[hang+h][lie+l] = 1 #从(i,j)开始改变qiang相应的位置状态，铺上横着铺的瓷砖
        for zhuandehang in range(a):
            for zhuandelie in range(b):
                newbrick.append(hang + zhuandelie + b * zhuandehang) #ans中加入该瓷砖铺好的方块编号
        ans.append(tuple(newbrick))
        puzhuan(ans) #递归调用铺下一个
        for h in range(a):
            for l in range(b):
                qiang[hang+h][lie+l] = 0 #从(i,j)开始改变qiang相应的位置状态，拆下横着铺的瓷砖
        ans.pop() #ans中去除该瓷砖铺好的方块编号
    return ans

if (m*n)%(a*b) != 0:
    print('墙面无法被铺满')
else:
    puzhuan(ans)
    print(ans)

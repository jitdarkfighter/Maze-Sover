from PIL import Image
import numpy as np
import heapq
import time 

start_time = time.time()
img= Image.open(r"Path to image")
img=img.convert("RGB")
rows,cols=5769,5769
L=[]
for i in range(rows):
    l=[]
    for j in range(cols):
        # if(img.getpixel((i,j))==(255,255,255,255)):
        if(img.getpixel((i,j))==(255,255,255)):
            l.append(0)
        else: 
            l.append(1)
    L.append(l)
print(L)


start=(1,0)
end=(5767,5768)
possible_ways=[(0,1),(1,0),(0,-1),(-1,0)]
def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def A_star(maze,start,end):
    rows,cols=len(maze), len(maze[1])
    open_list=[]
    heapq.heappush(open_list,(0,start))
    traversed={}
    g_score={start: 0}
    f_score={start: heuristic(start,end)}

    while open_list:
        _,cur=heapq.heappop(open_list)
        if(cur == end):
            ans=[]
            while cur in traversed:
                ans.append(cur)
                cur=traversed[cur]
            ans.append(start)
            return ans[::-1]
        
        for dx,dy in possible_ways:
            neighbour=(cur[0]+dx,cur[1]+dy)
            if 0<=neighbour[0]<rows and 0<=neighbour[1]<cols and maze[neighbour[0]][neighbour[1]] == 0:
                temp_g_score=g_score[cur]+1
                if neighbour not in g_score or temp_g_score<g_score[neighbour]:
                    traversed[neighbour] = cur
                    g_score[neighbour]= temp_g_score
                    f_score[neighbour]= temp_g_score+heuristic(neighbour,end)
                    heapq.heappush(open_list,(f_score[neighbour],neighbour))
    return ["no path"]

ans=A_star(L,start,end)
print(ans)


for i in ans:
    img.putpixel(i,(255,0,0))

img.save("ans.png")
print(f"TIME TAKEN : {time.time() - start_time}")
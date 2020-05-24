lstAB=[int(i) for i in input('Nhap vao 2 so A va N: ').strip().split(' ')]

ans=[]
for i in range(0,lstAB[0]):
    row=[]
    for j in range(0,lstAB[1]):        
        row.append(i*j)
    ans.append(row)

for i in range(len(ans)):
    a='\t'.join(str(x)for x in ans[i])+'\n'
    print(a)
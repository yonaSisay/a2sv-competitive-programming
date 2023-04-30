if __name__ == '__main__':
    n, m = map(int, input().split())
    res = []
    for row in range(n):
        res.append(list(input()))
    rows = []
    for i in range(len(res)):
        row = []
        for j in range(len(res[0])):
            row.append(res[i][j])
        rows.append(row)
        
    cols = []
    for i in range(len(res[0])):
        col = []
        for j in range(len(res)):
            col.append(res[j][i])
        cols.append(col)
    
    ans = []
    for i in range(len(res)):
        for j in range(len(res[0])):
            if rows[i].count(res[i][j]) == 1 and cols[j].count(res[i][j])  == 1:
                ans.append(res[i][j])
                
    print(''.join(ans))
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) ==0:
            return []
        col_s = 0;
        col_e = len(matrix[0]);
        row_s = 0;
        row_e = len(matrix);
        ret = [];
        while col_s<col_e and row_s<row_e:
            for j in range(col_s,col_e,1):
                #print(row_s,j)
                ret.append(matrix[row_s][j])
            for i in range(row_s+1,row_e-1,1):
                #print(i,col_e-1)
                ret.append(matrix[i][col_e-1])
            if (row_e-row_s)>1:
                for j in range(col_e-1,col_s-1,-1):
                    #print(row_e-1,j)
                    ret.append(matrix[row_e-1][j])
            if (col_e-col_s)>1:
                for i in range(row_e-2,row_s,-1):
                    #print(i,col_s)
                    ret.append(matrix[i][col_s])
            row_s+=1
            row_e-=1
            col_s+=1
            col_e-=1
        return ret
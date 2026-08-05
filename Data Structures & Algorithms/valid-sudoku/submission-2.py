class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ok = True 
        i = -1
        while ok and i<8:
            i += 1
            b = []
            l = []
            for j in range(9):
                l.append(board[j][i])
                b.append(board[ (i//3)*3 + j//3 ][ (i%3)*3 + j%3 ])

            k = -1
            while ok and k <9 :
                k += 1 
                ok = ok and l.count(str(k)) <=1 and board[i].count(str(k)) <=1 and b.count(str(k)) <=1

        return ok


            












        
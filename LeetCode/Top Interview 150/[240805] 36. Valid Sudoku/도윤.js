function isValidSudoku(board) {
    
    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const boxes = Array.from({ length: 9 }, () => new Set());

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            const num = board[r][c];
            if (num === '.') continue; 

            if (rows[r].has(num) || cols[c].has(num) || boxes[Math.floor(r / 3) * 3 + Math.floor(c / 3)].has(num)) {
                return false; 
            }

            rows[r].add(num);
            cols[c].add(num);
            boxes[Math.floor(r / 3) * 3 + Math.floor(c / 3)].add(num);
        }
    }

    return true;
}

const board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

console.log(isValidSudoku(board));

// ^^ 월요일 좋아 ^^
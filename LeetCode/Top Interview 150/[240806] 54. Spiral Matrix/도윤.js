/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let left = 0;
    let right = matrix[0].length - 1;
    let up = 0;
    let down = matrix.length - 1;
    const result = [];

    while (result.length < matrix.length + matrix[0].length) {
    
       for (let i = left; i <= right; i++) {
            result.push(matrix[up][i]);
       }
       left++;

       for (let i = up + 1; i <= down; i++) {
        result.push(matrix[i][right]);
       }

       up++
    }

    return result;
};

var matrix = [[1,2,3],[4,5,6],[7,8,9]];

spiralOrder(matrix);
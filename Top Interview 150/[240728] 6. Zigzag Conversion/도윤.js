/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {

    if(numRows === 1) return s;
    
    let idx = 0;
    let arrIdx = 0;
    let isUp = false;
    const arr = new Array(numRows).fill('');

    

    while(idx < s.length) {
        arr[arrIdx] += s[idx];


        if(isUp) {
            arrIdx--;
        } else {
            arrIdx++;
        }
        
        if(arrIdx === 0 || arrIdx === numRows - 1) {           
            isUp = !isUp;
        }
 
        idx++;
    }

    return arr.join("");  
};

convert("PAYPALISHIRING", 3);
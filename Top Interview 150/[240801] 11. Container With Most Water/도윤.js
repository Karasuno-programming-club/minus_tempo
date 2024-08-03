/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {

    
    let sp = 0;
    let ep = height.length - 1;

    let max = 0


    while(sp <= ep) {

        const area = (ep - sp) * (height[sp] > height[ep] ? height[ep--] : height[sp++]);

        if(max < area) { 
            max = area;
        } 
    }

    return max;

};
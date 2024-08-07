/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {

    let total = 0;
    let current = 0;
    let startIndex = 0;

    for (let i = 0; i < gas.length; i++) {
        
        const consumption = gas[i] - cost[i];
        total += consumption;
        current += consumption;

        if(current < 0) {
            current = 0;
            startIndex = i+1;
        }
    }

    if(total < 0)  {
        startIndex = -1;
    }

    return startIndex;  
};


var gas = [1,2,3,4,5], cost = [3,4,5,1,2];
canCompleteCircuit(gas, cost);
var canCompleteCircuit = function(gas, cost) {
    let curTank = 0, totalTank = 0, pos = 0;
    for(let i = 0; i < gas.length; i++){
        curTank += gas[i] - cost[i];
        totalTank += gas[i] - cost[i];
        if(curTank < 0){
            curTank = 0;
            pos = i+1;
        }
    }

    return totalTank < 0 ? -1 : pos;
};

// totalTank가 0보다 크면 이전 station도 지나올 수 있다는 얘기
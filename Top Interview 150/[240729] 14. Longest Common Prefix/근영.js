var longestCommonPrefix = function(strs) {
    let prefix = strs[0];
    let length = prefix.length;

    for(let i = 1; i < strs.length; i++){
        let s = strs[i];
        while(prefix !== s.slice(0, length)){
            length--;
            if(length === 0){
                return "";
            }
            prefix = prefix.slice(0, length);
        }
    }
    return prefix
};

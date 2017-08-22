function countPositives(arr){
    var pos = 0;
    for (var i = 0; i < arr.length; i++){
        while(arr[i] > 0){
            pos++;
        } 
    } arr[arr.length - 1] = pos;
    return arr;
}


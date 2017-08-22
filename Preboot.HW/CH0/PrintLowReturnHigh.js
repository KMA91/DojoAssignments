function PL(arr){
    var low = arr[0];
    var high = arr[0];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > high){
            high = arr[i];
        }
        if(arr[i] < low){
            low = arr[i];
        }
    } console.log("lowest value = " + low)
return high;    
}
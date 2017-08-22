function NumbersOnly(arr){
    var newarr = [];
    for(var i = 0; i < arr.length; i++){
        if(typeof arr[i] === "number" == true){
            newarr.push(arr[i]);
        }
    } return newarr;
}
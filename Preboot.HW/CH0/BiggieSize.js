function MIB(arr){
    
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            arr[i] = "big";
        }
    }console.log(arr);
}

MIB([-1,2,2]);
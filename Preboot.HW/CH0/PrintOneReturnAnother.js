function PO(arr){
    var StL = 0;
StL = arr[arr.length - 2];
console.log(StL);
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 1){
            return arr[i];
        }else{
            console.log("There is no odd value in your array")
        }
    }
}
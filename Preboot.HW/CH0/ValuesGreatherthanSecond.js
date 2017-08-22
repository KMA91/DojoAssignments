function Value(){
var arr = [1, 3, 5, 7, 9, 13];
var count = 0;

for(var i = 0; i < arr.length; i++){
    if(i === 3){
        continue;
    }
    if(arr[i]>arr[1]){
        console.log(arr[i]);
        count++;
    } 
}return count;
}
var param1 = 3;
var param2 = 5;
var param3 = 17;
var param4 = 9;

for (var x = param1; x <= param3; x = x + 3){
if(x % param4 === 0){
continue;
}
console.log(x);
}
for (var x = 1; x <= 100; x++){
if(x % 5 === 0){
  if (x % 10 !== 0){
    console.log("Coding");
    continue;
}else{
    console.log(x);
}
if (x % 10 === 0){
    console.log("Dojo");
}
}
}
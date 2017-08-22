function RC(quarters){
	var winning;
	var poss;
	if(quarters <= 0){
		poss = Math.random();
		while(poss > 0.01){
		winning = Math.floor(Math.random() * 100 + 50);
		console.log("You won " + winning);
		quarters+=winning;
		return quarters;
		}
	}else{
      console.log("No more quarters :(")
    }
}
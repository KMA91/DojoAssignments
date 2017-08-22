function RC(quarters){
	var poss;
	var win;
	quarters -= quarters;
	
	if(quarters <= 0){
		poss = Math.random;
		if(poss < 0.001){
			win = Math.floor(Math.random() * 100) + 50;
			console.log("You won " + win + " quarters!")
			quarters = quarters + win;
			console.log("You now have " + quarters + " quarters!")
		}else{
			console.log("Try again!");
	}else{
		console.log("Out of quarters :(");
}

RC();
      
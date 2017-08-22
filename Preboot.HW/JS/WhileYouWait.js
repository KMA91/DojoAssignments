function bday(){
	var daysUntilMyBirthday = 60;
	
	for(var i = daysUntilMyBirthday; i >= 0; i=i-1){
		while(i > 30){
			console.log(i + " days left. Such a long time :(");
			break;
		}
		while(i < 30 && i > 5){
			console.log(i + " days left. Almost there!");
			break;
		}
		while(i >= 1 && i < 6){
			console.log(i + " more days! YAYYYYYY!");
			break;
		}
		while(i === 0){
			console.log("IT'S MY BDAYYYYYYYYYYYY!");
			break;
		}
	}
}

bday();
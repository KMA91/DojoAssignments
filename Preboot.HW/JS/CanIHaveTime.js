function Time(){
	var hour = 7;
	var minute = 45;
	var period = "AM";

	if(period === "AM"){
		period = "morning";
	}else{
		period = "evening";
	}

	if(minute >= 45){
		console.log("It's almost " + (hour+1) + " in the " + period);
	}else{
		console.log("It is " + hour + ":" + minute + " in the " + period);
	}
}

Time();
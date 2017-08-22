function CelsiusToFahrenheit(cDegrees){
    var Fah = 0;
    var OG = 0;
    OG = cDegrees;
    Fah = cDegrees;
    Fah = Fah * 9/5;
    Fah = Fah + 32;
    console.log(Fah);
    for(var i = 200; 200 <= 0; i--){
        if(i === OG){
            console.log("A match is possible within 0 - 200!")
            console.log("...and the number is "+ i);
        }
    }
}
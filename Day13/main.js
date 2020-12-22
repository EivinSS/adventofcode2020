const fs = require('fs');

const lines = fs.readFileSync('numbers.txt', {encoding: 'utf-8'}).split('\n').filter(x => x);

//get all departure times in list. Jesses i could have done this in 4 lines of code i realised.
var departures = []
for (let i = 0; i < lines[1].length; i++) {
    if (!isNaN(lines[1][i])){
        var int1 = "";
        int1 = int1 + (lines[1][i]);
        var mybol = true
        var j = 1;
        while (mybol) {
            if (!isNaN(lines[1][i+j])) {
                int1 = int1 + (lines[1][i+j])
                j++;
            } else {
                i = i + j
                mybol = false
            }
        }
        departures.push(parseInt(int1));
    }
}

var number = parseInt(lines[0]);
var waitingTimes = [] 
for (let i = 0; i < departures.length; i++) {
    waitingTimes.push(((Math.floor(number/departures[i]) + 1) * departures[i]) - number)
}

console.log(waitingTimes)

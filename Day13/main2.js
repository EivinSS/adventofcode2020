/*  Im to lazy to make two lists and more code, so here is an explaination:

    First, i ran the script with a smaller set of the puzzle input, including 739.
    I iterate through the list with a step of 739, and a startpoint of negative the index of 739 in the list.
    Then i found the timestamp that matched this set of the puzzle input.
    The timestep was 34398423618.
    Then, i started the next iteration at this timestep. The key is to know which step to use in the next iteration when including all the puzzle input.
    If you multiply the numbers up until 739 you get 1534938432833. At each 'step' at this number, the sequence will repeat itself. And never before. Thats the magic of primes.
    So then the answer to the multiplication will be the new step in the iteration, and the inital timestamp will be 34398423618.
    Now we only check for the sequences which the numbers up until 739 will be in the correct order.
*/

const fs = require('fs');
var path = require("path");

const lines = fs.readFileSync(path.resolve(__dirname, 'numbers.txt'), {encoding: 'utf-8'}).split('\n').filter(x => x);

var departures = []
departures = lines[1].split(',');

var max = 0
var index_max = 0

for (let i = 0; i < departures.length; i++) {
    if ((departures[i]) == 'x') {
        //do nothing
    }
    else {
        departures[i] = parseInt(departures[i])
        if (departures[i] > max) {
            max = departures[i]
            index_max = i
        }
    }
}

var Found = false
var timestamp = 34398423618
//var timestamp = -index_max

while (!Found) {
    for (let i = 0; i < departures.length; i++) {
        if ((departures[i]) == 'x') {
            //do nothing
        }
        else {
            if ((timestamp+i) % parseInt(departures[i]) == 0) {
                if (i == (departures.length-1)) {
                    Found = true
                    console.log(timestamp)
                    break
                }
            }
            else {
                timestamp = timestamp + 1534938432833;
                //timestamp = timestamp + max
                break
            }
        }
    }
}

console.log(departures)
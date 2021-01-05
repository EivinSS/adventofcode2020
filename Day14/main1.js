const fs = require('fs');
var path = require("path");
const { start } = require('repl');

const lines = fs.readFileSync(path.resolve(__dirname, 'numbers.txt'), {encoding: 'utf-8'}).split('\n').filter(x => x);

var mask = ""
var mem = new Array(100000)

for (let i = 0; i < mem.length; i++) {
    mem[i] = 0;
}

for (let i = 0; i < lines.length; i++) {
    lines[i] = lines[i].replace(/(\r\n|\n|\r)/gm, "");
    if (lines[i].startsWith("mask")) {
        mask = lines[i].substring(lines[i].indexOf("=")+2)
    }
    if (lines[i].startsWith("mem")) {
        var binary = ((parseInt(lines[i].substring(lines[i].indexOf("=")+2))) >>> 0).toString(2);
        var lengty = binary.length
        for (let x = 0; x < (36-lengty); x++) {
            adding = "0"
            binary = adding.concat(binary)
        }
        var newBinary = ""
        for (let y = mask.length-1; y >= -1; y--) {
            if (mask.charAt(y) == 'X') {
                let letter1 = ""
                letter1 = binary.charAt(y)
                newBinary = letter1.concat(newBinary) 
            }
            if (mask.charAt(y) == '0') {
                newBinary = '0'.concat(newBinary)
            }
            if (mask.charAt(y) == '1') {
                newBinary = '1'.concat(newBinary)
            }
        }
        let startInd = lines[i].indexOf("[")
        let stopInd = lines[i].indexOf("]")
        let index = parseInt(lines[i].substring(startInd+1, stopInd))
        mem[index] = parseInt((newBinary), 2)
    }
}

var sum = 0
for (let i = 0; i < mem.length; i++) {
    sum += (mem[i])
}

console.log(sum)


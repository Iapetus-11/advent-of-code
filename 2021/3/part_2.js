const fs = require("fs");

const data = fs.readFileSync("input.txt", "utf8");

const lines = data.trim("\n").split("\r").join("").split("\n");

let oxy = null;
let co2 = null;

let ogLines = [...lines];
let lsLines = [...lines];

for (i = 0; i < lines[0].length; i++) {
    let ones = 0;
    let zeros = 0;

    ogLines.forEach(l => {
        if (l[i] === "0") zeros += 1;
        else ones += 1;
    });

    let mcb = ones >= zeros ? "1" : "0";

    ogLines = ogLines.filter(l => l[i] === mcb);

    if (!oxy && ogLines.length === 1) oxy = parseInt(ogLines[0], 2);

    ones = 0;
    zeros = 0;

    lsLines.forEach(l => {
        if (l[i] === "0") zeros += 1;
        else ones += 1;
    });

    lcb = zeros > ones ? "1" : "0";

    lsLines = lsLines.filter(l => l[i] === lcb);

    if (!co2 && lsLines.length === 1) co2 = parseInt(lsLines[0], 2);
}

console.log(oxy * co2);

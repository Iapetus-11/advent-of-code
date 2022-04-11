const fs = require("fs");

const lines = fs.readFileSync("input.txt", "utf8").trim("\n").replace(/\r/g, "").split("\n");

let gRate = "";
let eRate = "";

for (i = 0; i < 12; i++) {
    let ones = 0;
    let zeros = 0;

    lines.forEach(l => {
        if (l[i] === "0") zeros += 1;
        else ones += 1;
    });

    if (ones > zeros) {
        gRate += "1";
        eRate += "0";
    } else {
        gRate += "0";
        eRate += "1";
    }
}

console.log(`gRate: ${gRate}, eRate: ${eRate}`);
console.log(parseInt(gRate, 2) * parseInt(eRate, 2));

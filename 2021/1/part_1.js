const fs = require("fs");

const lines = fs.readFileSync("input.txt", "utf8").trim("\n").replace(/\r/g, "").split("\n");

const measurements = lines.map(n => parseInt(n, 10));

var last = measurements[0];
var increases = 0;

for (m of measurements.slice(1)) {
    if (m > last) increases++;

    last = m;
}

console.log(increases);

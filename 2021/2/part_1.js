const fs = require("fs");

const lines = fs.readFileSync("input.txt", "utf8").trim("\n").replace(/\r/g, "").split("\n");

let h = 0;
let d = 0;

for (l of lines) {
    let [a, v] = l.split(" ");

    v = parseInt(v, 10);

    switch(a) {
        case "forward":
            h += v;
            break;
        case "down":
            d += v;
            break;
        case "up":
            d -= v;
            break;
    }
}

console.log(h * d);

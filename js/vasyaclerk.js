// https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/
function tickets(peopleInLine) {
    var exchange = {};
    for (var i = 0; i < peopleInLine.length; i++) {
        // console.log(`Current bill is ${peopleInLine[i]}`);
        // console.log("    current exchange is");
        // console.log("    -----------------");
        // console.log(exchange);
        // console.log("    -----------------");
        if (peopleInLine[i] === 25) {
            if (exchange[peopleInLine[i]])
                exchange[peopleInLine[i]] += 1;
            else
                exchange[peopleInLine[i]] = 1;
        }
        if (peopleInLine[i] === 50) {
            if (exchange["25"] > 0) {
                exchange["25"] -= 1;
                if (exchange[peopleInLine[i]])
                    exchange[peopleInLine[i]] += 1;
                else
                    exchange[peopleInLine[i]] = 1;
            }
            else
                return "NO";
        }
        if (peopleInLine[i] === 100) {
            var summary = 0;
            if (exchange["50"] > 0) {
                exchange["50"] -= 1;
                summary += 50;
            }
            if (exchange["25"] > 0) {
                do {
                    exchange["25"] -= 1;
                    summary += 25;
                } while (summary < 75 && exchange["25"] > 0);
                if (summary !== 75)
                    return "NO";
            }
            else
                return "NO";
        }
    }
    return "YES";
}
//# sourceMappingURL=vasyaclerk.js.map
// https://www.codewars.com/kata/53f40dff5f9d31b813000774/
function recoverSecret(triplets) {
    var alphabet = [];
    for (var i = 0; i < triplets.length; i++) {
        for (var j = 0; j < triplets[i].length; j++) {
            if (!alphabet.includes(triplets[i][j])) {
                alphabet.push(triplets[i][j]);
            }
        }
    }
    var res = '';
    for (var j = 0; j < alphabet.length; j++) {
        for (var i = 0; i < alphabet.length; i++) {
            if (res.includes(alphabet[i])) {
                continue;
            }
            var tmp = nextLetter(triplets, alphabet[i], res);
            if (tmp) {
                res += tmp;
                break;
            }
        }
    }
    return res;
}
function nextLetter(triplets, lett, exclude) {
    var before = '';
    for (var i = 0; i < triplets.length; i++) {
        if (triplets[i][0] == lett) {
        }
        if (triplets[i][1] == lett) {
            if (!exclude.includes(triplets[i][0])) {
                before += triplets[i][0];
            }
        }
        if (triplets[i][2] == lett) {
            if (!exclude.includes(triplets[i][0])) {
                before += triplets[i][0];
            }
            if (!exclude.includes(triplets[i][1])) {
                before += triplets[i][0];
            }
        }
    }
    if (!before) {
        return lett;
    }
    return '';
}
//# sourceMappingURL=recoversecret.js.map
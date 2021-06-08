//https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7
module.exports = function kaprekarSplit(n) {
    var square = n * n;
    var str_square = String(square);
    for (var i = 0; i < str_square.length; i++) {
        var start = str_square.substr(0, i);
        var end = str_square.substr(i, str_square.length);
        if (Number(start) + Number(end) === n) {
            return i;
        }
    }
    return -1;
};

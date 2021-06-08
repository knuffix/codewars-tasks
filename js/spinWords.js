//https://www.codewars.com/kata/5264d2b162488dc400000001
module.exports = function spinWords(string) {
    var words = string.split(" ");
    var result = "";
    for (var i = 0; i < words.length; i++) {
        if (words[i].length >= 5) {
            result += words[i].split("").reverse().join("");
        }
        else {
            result += words[i];
        }
        if (i !== words.length - 1) {
            result += ' ';
        }
    }
    return result;
};

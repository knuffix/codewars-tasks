//https://www.codewars.com/kata/5a045fee46d843effa000070/
module.exports = function decomp(n) {
    var array = new Array(n).fill(n);
    var primeArr = {};
    array = array.map(function (cur, index) {
        return cur - index;
    });
    for (var i = 0; i < array.length; i++) {
        if (is_prime(array[i])) {
            primeArr[array[i]] = 0;
        }
    }
    for (var i = 0; i < array.length; i++) {
        for (var j in primeArr) {
            primeArr[j] += recursive_division_counter(array[i], Number(j));
        }
    }
    var result = "";
    for (var i in primeArr) {
        if (primeArr[i] > 1) {
            result += i + "^" + primeArr[i];
            result += " * ";
        }
        if (primeArr[i] == 1) {
            result += i + " * ";
        }
    }
    return result.slice(0, result.length - 3);
};
function recursive_division_counter(n, d) {
    var count = 0;
    if (d == 1) {
        return 0;
    }
    if (n % d == 0) {
        count += recursive_division_counter(n / d, d);
        count++;
    }
    else {
        return 0;
    }
    return count;
}
function is_prime(n) {
    for (var i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

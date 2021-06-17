//https://www.codewars.com/kata/514b92a657cdc65150000006
function solution(number) {
    if (number < 0) {
        return 0;
    }
    var sum = 0;
    for (var i = 0; i < number; i++) {
        var checked = false;
        if (i % 3 == 0) {
            sum += i;
            checked = true;
        }
        if (i % 5 == 0 && !checked) {
            sum += i;
        }
    }
    return sum;
}
//# sourceMappingURL=multiples_of_3_and_5.js.map
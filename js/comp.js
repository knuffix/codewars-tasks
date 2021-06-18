// https://www.codewars.com/kata/550498447451fbbd7600041c
function comp(arr1, arr2) {
    if (arr1 == null || arr2 == null) {
        return false;
    }
    if (arr1.length !== arr2.length) {
        return false;
    }
    var tmp = arr1.map(function (element) {
        return element * element;
    });
    var tmp2 = arr2.sort(function (a, b) { return a - b; });
    tmp = tmp.sort(function (a, b) { return a - b; });
    var is_found = true;
    tmp.forEach(function (element, index) {
        if (element !== tmp2[index]) {
            is_found = false;
        }
        if (!is_found)
            return;
    });
    return is_found;
}
var a1 = [121, 144, 19, 161, 19, 144, 19, 11];
var a2 = [
    11 * 11,
    121 * 121,
    144 * 144,
    19 * 19,
    161 * 161,
    19 * 19,
    144 * 144,
    19 * 19,
];
console.log(comp(a1, a2));
//# sourceMappingURL=comp.js.map
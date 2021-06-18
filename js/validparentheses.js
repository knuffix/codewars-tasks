//https://www.codewars.com/kata/52774a314c2333f0a7000688/
function validParentheses(parens) {
    var opened_par = 0;
    var closed_par = 0;
    var flag = true;
    parens.split("").forEach(function (element) {
        if (element == "(") {
            opened_par++;
        }
        if (element == ")") {
            closed_par++;
        }
        if (closed_par > opened_par) {
            flag = false;
            return;
        }
    });
    return flag && closed_par === opened_par;
}
//# sourceMappingURL=validparentheses.js.map
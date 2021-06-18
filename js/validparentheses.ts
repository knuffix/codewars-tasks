//https://www.codewars.com/kata/52774a314c2333f0a7000688/
function validParentheses(parens: string): boolean {
  let opened_par: number = 0;
  let closed_par: number = 0;
  let flag: boolean = true;
  parens.split("").forEach((element) => {
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

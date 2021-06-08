//https://www.codewars.com/kata/52fba66badcd10859f00097e
module.exports = function disemvowel(str: string): string {
  return str.replace(/[aeuio]/gi, "");
}

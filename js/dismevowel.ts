module.exports = function disemvowel(str: string): string {
  return str.replace(/[aeuio]/gi, "");
}

module.exports = function spinWords(string: string): string {
  let words = string.split(" ");
  let result = "";
  for (let i = 0; i < words.length; i++) {
    if (words[i].length >= 5) {
      result += words[i].split("").reverse().join("");
    } else {
      result += words[i];
    }
    if (i !== words.length - 1){
      result += ' ';
    }
    
  }
  return result;
}
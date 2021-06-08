//https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7
module.exports = function kaprekarSplit(n: number):number {
  let square = n * n;
  let str_square = String(square);
  for (let i = 0; i < str_square.length; i++) {
    const start = str_square.substr(0,i);
    const end = str_square.substr(i,str_square.length);
    if (Number(start) + Number(end) === n){
      return i;
    }
    
    
  }
  return -1
}
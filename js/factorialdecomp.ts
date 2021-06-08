//https://www.codewars.com/kata/5a045fee46d843effa000070/
module.exports = function decomp(n: number): string {
  let array = new Array(n).fill(n);
  let primeArr = {};
  array = array.map((cur, index) => {
    return cur - index;
  });
  for (let i = 0; i < array.length; i++) {
    if (is_prime(array[i])) {
      primeArr[array[i]] = 0;
    }
  }
  for (let i = 0; i < array.length; i++) {
    for (let j in primeArr) {
      primeArr[j] += recursive_division_counter(array[i], Number(j));
    }
  }
  let result = "";
  for (let i in primeArr) {
    if (primeArr[i] > 1) {
      result += `${i}^${primeArr[i]}`;
      result += " * ";
    }
    if (primeArr[i] == 1) {
      result += `${i} * `;
    }
  }
  return result.slice(0, result.length - 3);
};
function recursive_division_counter(n: number, d: number): number {
  let count = 0;
  if (d == 1) {
    return 0;
  }
  if (n % d == 0) {
    count += recursive_division_counter(n / d, d);
    count++;
  } else {
    return 0;
  }
  return count;
}
function is_prime(n: number): boolean {
  for (let i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

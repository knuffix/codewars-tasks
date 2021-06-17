//https://www.codewars.com/kata/514b92a657cdc65150000006

function solution(number: number): number {
  if (number < 0) {
    return 0;
  }
  let sum: number = 0;
  for (let i = 0; i < number; i++) {
    let checked: boolean = false;
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

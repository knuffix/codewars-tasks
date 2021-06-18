// https://www.codewars.com/kata/550498447451fbbd7600041c

function comp(arr1: number[], arr2: number[]): boolean {
  if (arr1 == null || arr2 == null) {
    return false;
  }
  if (arr1.length !== arr2.length) {
    return false;
  }
  let tmp: number[] = arr1.map((element) => {
    return element * element;
  });
  let tmp2: number[] = arr2.sort((a, b) => a - b);
  tmp = tmp.sort((a, b) => a - b);
  let is_found: boolean = true;
  tmp.forEach((element, index) => {
    if (element !== tmp2[index]) {
      is_found = false;
    }
    if (!is_found) return
  });

  return is_found;
}

let a1 = [121, 144, 19, 161, 19, 144, 19, 11];
let a2 = [
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

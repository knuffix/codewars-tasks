//https://www.codewars.com/kata/5544c7a5cb454edb3c000047

function bouncingBall(h: number, bounce: number, window: number): number {
  if (h <= 0) return -1;
  if (bounce <= 0 || bounce >= 1) return -1;
  if (window >= h) return -1;
  let bounce_height: number = h;
  let count: number = 1;
  console.log(`Drop ball from ${h}`)
  do {
    count += 2;
    bounce_height *= bounce;
    console.log(`ball height is ${bounce_height}`)
  } while (bounce_height > window);
  return count - 2;
}
console.log(bouncingBall(3.0, 0.66, 1.5));

#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log(1);
} else {
  let i = Number(process.argv[2]);
  let fact = 1;
  while (i > 0) {
    fact *= i;
    i--;
  }
  console.log(fact);
}

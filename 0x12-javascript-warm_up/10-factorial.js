#!/usr/bin/node
const factorial = function (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(--num);
};
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}

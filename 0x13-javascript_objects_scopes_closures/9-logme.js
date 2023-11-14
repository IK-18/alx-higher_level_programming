#!/usr/bin/node
let numb = 0;
exports.logMe = function (item) {
  console.log(numb + ': ' + item);
  numb++;
}

#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  let i = list.length - 1;
  for (let j = 0; j < list.length; j++) {
    arr[j] = list[i];
    i--;
  }
  return arr;
};

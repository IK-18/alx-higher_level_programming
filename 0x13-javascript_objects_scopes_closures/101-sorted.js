#!/usr/bin/node
const dict = require('./101-data').dict;
const pairs = Object.entries(dict);
const keys = [...new Set(Object.values(dict))];
const newDict = {};
for (const key of keys) {
  let list = [];
  for (const pair of pairs) {
    if (pair[1] === key) {
      list.push(pair[0]);
    }
  }
  newDict[key] = list;
}
console.log(newDict);

"use strict";

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const sum = arr.reduce(function (acc, val, key, arr) {
  return acc + val;
});
console.log(sum);

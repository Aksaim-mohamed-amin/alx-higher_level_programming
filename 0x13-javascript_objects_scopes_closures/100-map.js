#!/usr/bin/node
/* Imports an array and computes a new array. */

const list = require('./100-data').list;
const newList = list.map((ele, index) => ele * index);

console.log(list);
console.log(newList);

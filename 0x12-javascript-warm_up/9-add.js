#!/usr/bin/node
/* return the addittion of two argument */

function add (a, b) {
  return a + b;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));

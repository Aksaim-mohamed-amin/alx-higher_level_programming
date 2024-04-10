#!/usr/bin/node
const number = process.argv[2];
function factorial (a) {
  if (a === 0) return (1);
  else return (a * factorial(a - 1));
}

if (isNaN(number)) console.log(1);
else console.log(factorial(number));

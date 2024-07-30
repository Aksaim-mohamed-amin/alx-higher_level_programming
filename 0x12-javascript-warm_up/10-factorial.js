#!/usr/bin/node
/* Comput the factorial of a number */

function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  console.log(factorial(process.argv[2]));
}

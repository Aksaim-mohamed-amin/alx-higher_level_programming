#!/usr/bin/node
const numbers = process.argv;

if (numbers.length < 3) console.log(0);
else {
  let first = -Infinity;
  let second = -Infinity;

  for (let i = 2; i < numbers.length; i++) {
    const current = parseInt(numbers[i]);

    if (current > first) {
      second = first;
      first = current;
    } else if (current > second && current !== first) second = current;
  }

  console.log(second !== -Infinity ? second : 0);
}

#!/usr/bin/node
const argsLength = process.argv.length;
if (argsLength < 3) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else if (argsLength > 3) {
  console.log('Arguments found');
}

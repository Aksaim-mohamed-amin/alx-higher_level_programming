#!/usr/bin/node

/**
 * Prints the number of arguments already printed and the new argument value.
 */
const str = [];
exports.logMe = function (item) {
  str.push(item);
  console.log(str.length - 1 + ': ' + str[str.length - 1]);
};

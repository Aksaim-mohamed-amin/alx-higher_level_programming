#!/usr/bin/node

/**
* Returns the reversed version of a list.
*/
exports.esrever = function (list) {
  const arr = [];
  for (let i = 0; i < list.length; i++) {
    arr[i] = list[list.length - i - 1];
  }
  return (arr);
};

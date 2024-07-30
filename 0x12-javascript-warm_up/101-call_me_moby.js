#!/usr/bin/node
/* Executes x times a function. */
exports.callMeMoby = function (n, f) {
  for (let i = 0; i < n; i++) {
    f();
  }
};

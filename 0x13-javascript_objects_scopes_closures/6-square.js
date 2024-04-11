#!/usr/bin/node

const originalSquare = require('./5-square');

/**
 * Represents a square.
 */
class Square extends originalSquare {
  /**
   * Prints the rectangle using the character c.
   */
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) { console.log(c.repeat(this.width)); }
  }
}

module.exports = Square;

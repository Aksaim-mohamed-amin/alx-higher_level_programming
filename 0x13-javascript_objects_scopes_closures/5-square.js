#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Represents a square.
 */
class Square extends Rectangle {
  /**
   * Create a square with the given .
   * @param {number} size - The width and the height of the square.
   */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

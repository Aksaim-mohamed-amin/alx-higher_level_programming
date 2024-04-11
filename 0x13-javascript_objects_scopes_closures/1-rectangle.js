#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  /**
   * Create a rectangle with the given width and height.
   * @param {number} width - The width of the rectangle.
   * @param {number} height - The height of the rectangle.
   */
  constructor (width, height) {
    this.width = width;
    this.height = height;
  }
}

module.exports = Rectangle;

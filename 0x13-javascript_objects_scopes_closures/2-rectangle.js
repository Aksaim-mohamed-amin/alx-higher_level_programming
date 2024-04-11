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
  constructor (w, h) {
    if (w > 0)
      this.width = w;
    if (h > 0)
    this.height = h;
  }
}

module.exports = Rectangle;

#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  /**
   * Create a rectangle with the given width and height.
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }

  /**
   * Print the rectangle to the console.
   */
  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  /**
   * Rotate the rectangle by exchanging the width and height.
   */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /**
   * Double the width and height of the rectangle.
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

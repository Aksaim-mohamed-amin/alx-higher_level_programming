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
}

module.exports = Rectangle;

#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // Trying to use while loop
    let i = 0;
    while (i < this.height) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
      i++;
    }
  }
};

#!/usr/bin/node

exports.converter = function (base) {
  // used arrow functn to create another function that takes number as parameter
  return number => number.toString(base);

//   alternative:
//   return function (number) {
//     return number.toString(base);
//   }
};

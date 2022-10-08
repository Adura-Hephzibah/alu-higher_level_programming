#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) { count++; }
  }
  return count;

//   return list.reduce((accumulator, current) => {
//     const occurrence = (current === searchElement) ? 1 : 0;
//     return accumulator + occurrence;
//   }, 0);
};

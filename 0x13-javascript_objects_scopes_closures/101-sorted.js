#!/usr/bin/node
/* Write a script that imports a dictionary of occurrences by user id and
   computes a dictionary of user ids by occurrence.

   Your script must import dict from the file 101-data.js
   In the new dictionary:
     * A key is a number of occurrences
     * A value is the list of user ids
   Print the new dictionary at the end
*/
const dict = require('./101-data.js').dict;
// { '89': 1, '90': 2, '91': 1, '92': 3, '93': 1, '94': 2 }
console.log(dict);

const listValues = [...new Set(Object.values(dict))]; // Obtain unique elements
// [ 1, 2, 3 ]
console.log(listValues);
const newDict = new Map();

for (const current in listValues) {
  const userArr = [];
  for (const key in dict) {
    if (dict[key] === listValues[current]) userArr.push(key);
  }
  newDict.set(listValues[current], userArr);
}
console.log(newDict);

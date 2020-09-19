#!/usr/bin/node
// function that increments and calls a function.
exports.addMeMaybe = function (x, theFunction) { return (theFunction(++x)); };

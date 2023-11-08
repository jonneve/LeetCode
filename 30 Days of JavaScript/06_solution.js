/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {

    // .filter method where the test condition is the fn function which evaluates truthiness of each element and returns a filter array
    return arr.filter(fn);
};
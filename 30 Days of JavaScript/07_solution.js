/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {

    // initialise accum to init value
    let accum = init;

    // if nums array has 1 or more element, loop through and set value of accum to the output of the function
    // else accum is set to init value, then return accum
    if (nums.length >= 1) {
        for (let i = 0; i < nums.length; i++) {
            accum = fn(accum, nums[i]);
        }
    } else {
        accum = init;
    }

    return accum;
};
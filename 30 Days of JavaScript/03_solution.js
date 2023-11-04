/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {

    // toBE/notToBe functions that throw relevant errors if 2nd value is/is not type equivelant  to 1st value
    return {
        toBe: function (val2) {
            if (val2 === val) {
                return true
            }
            else {
                throw new Error("Not Equal")
            }
        },

        notToBe: function (val2) {
            if (val2 !== val) {
                return true
            }
            else {
                throw new Error("Equal")
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
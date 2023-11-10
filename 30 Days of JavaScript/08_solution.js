/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {

    return function (x) {

        // initialise result to be value of x
        let result = x;

        // if an empty list just return result (whihc is x), else perform a for loop seeting result to be the product fo each function
        // use a -- decrement and init i to be length of list -1 to perform right to left application of functions from list 
        if (functions.length >= 1) {
            for (let i = functions.length - 1; i >= 0; i--) {
                result = functions[i](result);
            }
        }

        return result;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
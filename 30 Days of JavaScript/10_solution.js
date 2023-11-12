/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {

    // bool to track if function has been previously called
    let called = false;

    return function (...args) {

        // if called return undefined, else return the fn function called with args and set called to be true 
        if (called) {
            return undefined;
        } else {
            called = true;
            return fn(...args);
        }

    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
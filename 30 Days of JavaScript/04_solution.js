/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {

    // set counter initial value to init
    var counter = init;

    // functions to increment, decrement using prefix increment and reset where reset sets counter back to initial init value
    function increment() {
        return ++counter;
    }

    function decrement() {
        return --counter;
    }

    function reset() {
        counter = init;
        return counter;
    }

    // return expected functions
    return {
        increment, decrement, reset
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
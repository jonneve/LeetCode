/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {

    // await the result of both promises then assign them to vars, retrun the sum of these vars    
    let [promise1_val, promise2_val] = await Promise.all([promise1, promise2]);

    return promise1_val + promise2_val;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
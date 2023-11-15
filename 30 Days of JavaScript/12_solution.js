/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {

    // new promise that sets timeout to the amount of millis, awaits then promise executes on resolve
    return new Promise(resolve => setTimeout(resolve, millis));

}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
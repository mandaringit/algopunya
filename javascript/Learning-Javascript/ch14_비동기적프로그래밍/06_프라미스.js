function countdown(seconds) {
  return new Promise(function (resolve, reject) {
    for (let i = seconds; i >= 0; i--) {
      setTimeout(function () {
        if (i === 13) return reject(new Error("Oh My God"));
        if (i > 0) console.log(i + '...');
        else resolve(console.log('Go!!'))
      }, (seconds - i) * 1000)
    }
  })
}

countdown(14)
  .then(
    function () {
      console.log("countdown completed successfully");
    },
  ).catch(
  function (err) {
    console.log("countdown experienced an error :" + err.message)
  },
);
let self = function () {
  console.log('a');
  return function () {
    console.log('b');
  }
};

self = self();
self();
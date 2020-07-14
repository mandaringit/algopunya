function a() {
  console.log('a: calling b');
  b();
  console.log('a: done');
}

function b() {
  console.log('b: calling c');
  c();
  console.log('b: done');
}

function c() {
  console.log('c: throwing error');
  throw new Error('c error');
  console.log('c: Done');
}

function d() {
  console.log('d: calling c');
  c();
  console.log('d: done');
}

try {
  a();
} catch (e) {
  console.log(e.stack)
}

try {
  d();
} catch (e) {
  console.log(e.stack)
}
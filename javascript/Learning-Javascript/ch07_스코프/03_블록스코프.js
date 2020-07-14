// let과 const는 식별자를 블록 스코프에 선언한다.

console.log('before block');
{
    console.log('inside block');
    const x = 3;
    console.log(x);
}
console.log(`outside block; x=${x}`);

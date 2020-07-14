// {
//     // block 1
//     const x = 'blue';
//     console.log(x);
// }
//
// console.log(typeof x);
// {
//     //block2
//     const x = 3;
//     console.log(x);
// }
// console.log(typeof x);


{
    let x = 'blue';
    console.log(x);
    {
        let x = 3;
        console.log(x);
    }
    console.log(x);
}
console.log(typeof x);
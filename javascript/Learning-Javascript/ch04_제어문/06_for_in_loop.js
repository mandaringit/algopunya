// for .. in 루프는 객체의 프로퍼티에 루프를 실행하도록 설계됨
// for (variable in object)
//     statement

const player = {name:'Thomas',rank:'Midshipman',age:25};
for (let prop in player){
    if (!player.hasOwnProperty(prop)) continue;
    console.log(prop + ': ' + player[prop]);
}
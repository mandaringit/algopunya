const year = new Date().getFullYear();
if (year % 4 !== 0) console.log(`${year} is NOT a leap year`);
else if (year % 100 !== 0) console.log(`${year} IS a leap year`);
else if (year % 400 !== 0) console.log(`${year} is NOT a leap year`);
else console.log(`${year} IS a leap year`);

// 이 코드를 10번, 100번 실행해야한다면...
// 그리고 콘솔이 기록하는 메세지를 바꿔야한다면... ?

// 서브루틴으로 해결하자.
function printLeapYearStatus(){
  const year = new Date().getFullYear();
  if (year % 4 !== 0) console.log(`${year} is NOT a leap year`);
  else if (year % 100 !== 0) console.log(`${year} IS a leap year`);
  else if (year % 400 !== 0) console.log(`${year} is NOT a leap year`);
  else console.log(`${year} IS a leap year`);
}



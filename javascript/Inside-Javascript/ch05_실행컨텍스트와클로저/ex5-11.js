// 변수가 전역에 노출되어 있다.

const buffAr = [
  'I am ',
  '',
  '. I live in ',
  '',
  '. I\'am ',
  '',
  ' years old.',
]

function getCompletedStr(name, city, age) {
  buffAr[1] = name;
  buffAr[3] = city;
  buffAr[5] = age;

  return buffAr.join('');
}

const str = getCompletedStr('zzoon', 'seoul', 16);
console.log(str);

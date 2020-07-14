function f(x) {
    return `in f: x=${x}`
}

console.log(f()); // 변수 미 할당시 undefined 리턴

// 매개변수 해체 (객체)
function getSentence({subject, verb, object}) {  // 유효한 식별자여야 한다. 없으면 undefined.
    return `${subject} ${verb} ${object}`
}

const o = {
    subject: "I",
    verb: "love",
    object: "javascript"
};

console.log(getSentence(o));

// 매개변수 해체 (배열)
function getSentence2([subject, verb, object]) {
    return `${subject} ${verb} ${object}`
}

const arr = ["I", "Love", "Javascript"];
console.log(getSentence2(arr));

// 확산연산자를 써서 남는 매개변수 이용 가능
function addPrefix(prefix, ...words) {
    const prefixedWords = [];
    for (let i = 0; i < words.length; i++) {
        prefixedWords[i] =prefix + words[i]
    }
    return prefixedWords
}

console.log(addPrefix("con","verse","vex"));

// 매개변수에 기본값 할당
function f3(a,b="default",c=3) {
    return  `${a} - ${b} - ${c}`
}
console.log(f3(5,6,7));
console.log(f3(5,6));
console.log(f3(5));
console.log(f3());
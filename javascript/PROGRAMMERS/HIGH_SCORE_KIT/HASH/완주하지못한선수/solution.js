function solution(participant, completion) {
  let answer = "";
  const persons = {};
  for (let person of participant) {
    persons[person] ? persons[person] += 1 : persons[person] = 1
  }

  for (let person of completion) {
    persons[person] -= 1;
    if (persons[person] === 0) {
      delete persons[person]
    }
  }

  for (let person in persons) {
    if (persons[person] > 0) {
      answer = person;
    }
  }

  return answer
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
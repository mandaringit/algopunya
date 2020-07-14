// filter는 이름이 암시하듯, 배열에서 필요한 것들만 남길 목적으로 만들어졌다.
// map과 마찬가지로 사본을 반환하여 새 배열에는 필요한 요소만 남는다.

const cards = [];
for (let suit of ['H', 'C', 'D', 'S']) {
    for (let value = 1; value <= 13; value++) {
        cards.push({suit, value});
    }
}

console.log(cards.filter(card => card.value === 2));
console.log(cards.filter(card => card.suit === 'D'));
console.log(cards.filter(card => card.value > 10));
console.log(cards.filter(card => card.value > 10 && card.suit === 'H'));


// map + filter
let cardToString;
{
    const suits = {'H': '\u2665', 'C': '\u2663', 'D': '\u2666', 'S': '\u2660'};
    const values = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'};
    cardToString = (c) => {
        for (let i = 2; i <= 10; i++) values[i] = i;
        return values[c.value] + suits[c.suit];
    }
}
console.log(cards.filter(card => card.value === 2).map(cardToString));
console.log(cards.filter(card => card.value > 10 && card.suit === 'H').map(cardToString));

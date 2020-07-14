export class Kata {
  static getCount(str: string) {
    const vowels: string[] = ['a', 'e', 'i', 'o', 'u'];
    let count: number = 0;

    for (let char of str) {
      console.log(vowels.includes(char));
    }
    return count;
  }
}

Kata.getCount('abracadabra');

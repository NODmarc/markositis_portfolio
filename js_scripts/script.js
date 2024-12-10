const VOWELS = ["a", "e", "i", "o", "u"];

function countVowels(text) {
    const count = text.match(/[aeiou]/gi).length;
    return console.log(count)

}

console.log("Example:");
console.log(countVowels("typEscript"))
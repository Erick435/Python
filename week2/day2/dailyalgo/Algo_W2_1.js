/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const stringrandom = "helloootherreee"

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */

// //MY ANSWER USING (SPLIT, SPLICE, JOIN)
// function stringDedupe(str) {
//     sentences = str.split('');
//     for (var i = 0; i < sentences.length; i++){
//         for (var j = i + 1; j < sentences.length; j++){
//             if(sentences[i] == sentences[j]){
//                 sentences.splice([j],1);
//             }
            
//         }
//     }
//     return sentences.join('')
// }

//INSTRUCTOR'S ANSWER
function stringDedupe(str){
    let distinctStr = "";
    const seen = {};

    for (let i = 0; i <= str.length - 1; i++){
        if (!seen[str[i]]){
            distinctStr += str[i];
            seen[str[i]] = true;
        }
    }
    return distinctStr;
}

console.log(stringDedupe(stringrandom))

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));

/*******************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str_1 = "hello";
const expected_1 = "olleh";

const str_2 = "hello world";
const expected_2 = "olleh dlrow";

const str_3 = "abc def ghi";
const expected_3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    const words = str.split(" ");
    let wordsReversed = "";

    for (const word of words){
        let reversedWord = "";

        for(let i = word.length - 1; i >= 0; i--){
            reversedWord += word[i];
        }
        if (wordsReversed.length > 0){
            reversedWord = " " + reversedWord;
        }
        wordsReversed += reversedWord;
    }
    return wordsReversed;
}

console.log(reverseWords(str_1))
console.log(reverseWords(str_2))
console.log(reverseWords(str_3))
/***********************************/

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const string1 = "This is a test";
const expected01 = "test a is This";

const string2 = "hello";
const expected02 = "hello";

const string3 = "   This  is a   test  ";
const expected03 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {
    if (wordsStr == false){
        return wordsStr;
    }

    const words = wordsStr .split(" ");
    let reversedWordOrder = "";
    console.log(words);

    for (let i = words.length - 1; i >= 0; i--){
        if (words[i] === ""){
            continue;
        }
        if(reversedWordOrder.length > 0){
            reversedWordOrder += " ";
        }
        reversedWordOrder += words[i];
    }
    return reverseWordOrder;
}

console.log(reverseWordOrder(string1))
console.log(reverseWordOrder(string2))
console.log(reverseWordOrder(string3))
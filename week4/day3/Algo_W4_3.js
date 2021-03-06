/* 
Recursively reverse a string
helpful methods:
str.slice(beginIndex[, endIndex])
returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
// function reverseStr(str) { 
//     if (str.length === ""){
//         return str;
//     }
//     var lastChar = str.slice(str.length - 1);
//     return lastChar + reverseStr(str.slice(0, str.length - 1))
// }

function reverseStr2(str = ""){
    if (str === ""){
        return "";
    }
    const strWithoutFirstChar = str.slice(1);
    const firstChar = str[0];

    return reverseStr2(strWithoutFirstChar) + firstChar;
}


console.log(reverseStr2("World"))
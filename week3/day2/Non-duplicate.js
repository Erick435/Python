/*Given an array of integers
return the first integer from the array that is not repeated anywhere else
If there are multiple non-repeated integers in the array,
the "first" one will be the one with the lowest index.
*/

const nums1 = [3, 5, 4, 3, 4, 6, 5];
const expected1 = 6;

const nums2 = [3, 5, 5];
const expected2 = 3;

const nums3 = [3, 3, 5];
const expected3 = 5;

const nums4 = [5];
const expected4 = 5;

const nums5 = [];
const expected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
// function firstNonRepeated(nums) {        NOT FULLY FUNCTONING
//     var count = [];
//     var single = [];

//     if (nums.length > 1){

//         for (var i = 0; i < nums.length - 1; i++){
//             for (var j = i + 1; j < nums.length; j++){
//                 if (nums[i] == nums[j]){
//                     count.push(nums[i]);
//                 }
//                 else if(nums[i] != nums[j]){
//                     single.push(nums[i]);
//                 }
//             }
//         }
//         return single[single.length - 1];
//     }
//     else if (nums.length < 1){
//         return null;
//     }
//     else {
//         return nums[0]
//     }
// }

function firstNonRepeated(nums){
    var freq = {};
    for (var num of nums){
        if (freq[num]){
            freq[num]++;
        }
        else {
            freq[num] = 1;
        }
    }

    //obj key order is not guaranteed (unless using a Map instance)
    // loop back through nums for the proper of elements
    for (var num of nums){
        if(freq[num]===1){
            return num;
        }
    }
    
    return null; //all duplicates
}

console.log(firstNonRepeated(nums1))
console.log(firstNonRepeated(nums2))
console.log(firstNonRepeated(nums3))
console.log(firstNonRepeated(nums4))
console.log(firstNonRepeated(nums5))
function rotateArray(arr, shiftBy){
    //modify arr instead of creating a new array
    var lastItem = arr[arr.length -1];
    for(var i = arr.lenth-1; i > 0; i--){
        arr[i] = arr[i - shiftBy];
        // console.log(arr);
    }
    arr[0] = lastItem;
    return arr;
}

console.log(rotateArray([1,2,3,4,5, 6], 2));

// console.log(rotateArray([1,2,3,4,5], 1) == (5,1,2,3,4));
// console.log(rotateArray([1,2,3,4,5], 2) == (4,5,1,2,3));
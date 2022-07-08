function swapPairs(arr){
    if (arr.length <= 1){
    return arr;
    }

    for (var i = 0; i < arr.length; i += 2){
      if(i + 1 < arr.length){
        var temp = arr[i];
        arr[i] = arr[i + 1]
        arr[i + 1] = temp;
      }
    }
  return arr;
  }

  function swapPairs2(arr) {
    for (let i = 1; i < arr.length; i += 2) {
        let temp = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

      console.log(swapPairs([1, 2,3,4,5,6])) // [2, 1, 4, 3, 6, 5]
      console.log(swapPairs([1,2,3,undefined, 5, 6, 7, 8]))  //[2, 1, undefined, 3, 6, 5, 8, 7]
      console.log(swapPairs2([1, 2, 3, 4, 5])) // [2, 1, 4, 3, 5]
      // console.log(swarpPairs([9, 1, 6, 3, 0, 12, 9, 4, 5]))    //[1, 9, 6, 3, 12, 0, 4, 9, 5]
      // console.log(swarpPairs(["apple", "pear", "avocado", "banana"])) //[pear, apple, banana, avocado]
    




    function deduplicateSortedArray(arr){
        let tempArray = [];
        for (let i = 0; i < arr.length; i++){
            if(arr[i] != arr[i + 1]){
                tempArray.push(arr[i]);
            }
        }
        arr.length = 0;
        for (const x of tempArray){
            arr.push(x);
        }
    }

let x = [0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6]
deduplicateSortedArray(x);
console.log(x);
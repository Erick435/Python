// function balance(arr){
//     var left = 0;
//     var right = 0;
//     var leftsum =  0;
//     var rightsum= 0;
    
//     for(var i = 0; i < arr.length; i++){
//         left = arr[i];
//         // console.log(left)
//         leftsum = leftsum + left;
//         for (var j = i + 1; j < arr.length - 1; j++){
//             right = arr[j]
//             rightsum = rightsum + right;
//             if(leftsum == rightsum){
//                 console.log("it equals!")
//                 console.log(leftsum + rightsum)
//             }
//             else{
//                 return -1;
//                 console.log(leftsum + " " + rightsum)
//             }
//         }
// }
// }

// balance([3, 4, 9, 2, 4, -2, 3])

function arrayBalanceIndex(arr){
    if(arr.length <= 2){
        return -1;
    }

    for(var i = 0; i < arr.length; i++){
        //i represents the index of a given array 
        for(var j = 0; j < arr.length; j++){
            var leftitems = 0;
            var rightitems = 0;
            if (j < i){
                //item with index j is on the left
                leftitems += arr[j]
            }
            else if(j > i){
                //item with index j is on the right
                rightitems += arr[j]
            }
        }
        if (leftitems == rightitems){
            return i;
        }
    }
    return -1;
}

arrayBalanceIndex([3, 4, 9, 2, 4, -2, 3])
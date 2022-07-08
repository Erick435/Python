// function selectionSort(arr) {
//     for (var i = arr.length - 1; i >= 1; i--){
//         for (var j = i - 1; j >= 0; j--){
//         var temp; 
//         if (arr[i] < arr[j]){
//         temp = arr[i]
//         arr[i] = arr[j]
//         arr[j] = temp
//         }
//         }
//     }
//     return arr
// }

numbersval = [5, 4, 3, 2, 1]
second = [-3, 36, 8 , 35, 16, 2]

function selectionSort(arr) {

    for (var i = arr.length - 1; i >= 0; i--) {

        var maxNumber = arr[0];
        var maxPosition = 0;

        for (var j = 0; j <= i; j++) {
            if (arr[j] > maxNumber) {
                maxNumber = arr[j];
                maxPosition = j;
            }
        }

        var temp = arr[i];
        arr[i] = maxNumber;
        arr[maxPosition] = temp;

    }

    return arr;
}



selection_sort(numbersval);
selection_sort(second);
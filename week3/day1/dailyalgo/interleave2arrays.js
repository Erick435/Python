array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]


function interleaveArrays(arrayA, arrayB) {

    var results = [];
    if (arrayA.length < arrayB.length) {

        for (let i = 0; i < arrayA.length; i++) {
            results.push(arrayA[i]);
            results.push(arrayB[i]);
        }
        if (arrayA.length < arrayB.length) {
            for (let j = arrayA.length; j < arrayB.length; j++) {
                results.push(arrayB[j]);
            }
        }
    }
    else {
        for (let i = 0; i < arrayB.length; i++) {
            results.push(arrayA[i]);
            results.push(arrayB[i]);
        }
        if (arrayA.length > arrayB.length) {
            for (let j = arrayB.length; j < arrayA.length; j++) {
                results.push(arrayA[j]);
            }
        }
    }
    return results;
}
console.log(interleaveArrays(array1, array2))
function findMissingValue(input){

    if (input.length <= 0){
        return undefined;
    }

    var minimumItem = input[0];
    var maximumItem = input[0];
    var sumOfItems = 0;

    for(var i = 0; i < input.length; i++){

        sumOfItems += input[i]

        if (input[i] < minimumItem){
            minimumItem = input[i]
        }
        else if (input[i] > maximumItem){
            maximumItem = input[i]
        }
    }
    var expectedSum = 0;
    for (var j = minimumItem; j <= maximumItem; j++){
        expectedSum += j;
    }

    return expectedSum - sumOfItems;
}
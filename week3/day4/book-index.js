pages1 = [1, 2, 3, 6, 7, 9, 11, 12, 13, 17]
pagespractice = [1, 2, 3, 5, 10]


/*
function bookIndex(pages) { //Seans group work
    var strArr = [];
    var str = "";

    for (var i = 0; i < pages.length; i++) {
        var seqStart = pages[i]
        var seqEnd = undefined;

        for (var j = i + 1; j < pages.length; j++) {
            if (pages[j] == pages[j - 1] + 1) {
                seqEnd = pages[j];
                if (j == pages.length - 1) {
                    i = j;
                    break;
                }
            } else if (seqEnd == undefined) {
                i = j - 1;
                break;
            } else {
                i = j - 1;
                break;
            }
        }
        if (seqEnd != undefined) {
            strArr.push('' + seqStart + '-' + seqEnd)
        } else {
            strArr.push('' + seqStart)
        }
    }
    for (var k = 0; k < strArr.length; k++) {
        if (k == strArr.length - 1) {
            str += strArr[k]
        } else {
            str += strArr[k] + ", ";
        }
    }

    return str;

} */


function bookIndex(pages){
    var strarray = [];
    for(var i = 0; i < pages.length; i++){
        var left = pages[i];
        var right = pages[i];

        while (pages[i] + 1 == pages[i + 1]){
            i++;
            right = pages[i];
        }

        if (left == right){
            strarray.push(left.toString());
        }
        else{
            // strarray.push(left + '-' + right);
            strarray.push(`${left} - ${right}`);
        //Python: strList.append(f"{left} - {right})
        }
    }
    
    // return strarray.join(', '); //not available in all languages
    return buildIndexString(strarray);
}


function buildIndexString(arr){
    var output = ''; 
    for (i in arr){
        output += arr[i];
        if(i !=arr.length - 1){
            output += ', ';
        }
    }
    return output;
}

console.log(bookIndex(pagespractice))
console.log(bookIndex(pages1))
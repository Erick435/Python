function bubbleSort(arr) {
  
    for(var i = 0; i < arr.length - 1; i++){
        for(var j = i + 1; j < arr.length; j++){
          if (arr[i] > arr[j]){
            var temp;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
          
            
          }
        }
        
    }
    return arr;
    }

bubbleSort([3,5,2,7,1,8])

//OR

function bubbleSort2(arr) {
    var temp;
    for(var i=0; i<arr.length; i++){
        for(var j=0; j<arr.length-i; j++){
            if(arr[j]>arr[j+1]){
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        }
      }
    }
    return arr
  } 

bubbleSort2([3,5,6,2,1,8])
console.log("Hello there");
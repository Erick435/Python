//recursions

function sigma(n) {
    var sum = 0;
    var i = 0;
    while (i <= n) {
        sum += i;
        i++;
    }
    return sum;
}

console.log(sigma(4))


function recursiveFactorial(input) {

    if (input <= 1) {
        return 1;
    }
    return input * recursiveFactorial(input - 1);
}

console.log(recursiveFactorial(5))
console.log(recursiveFactorial(4))
console.log(recursiveFactorial(3))
console.log(recursiveFactorial(2))
console.log(recursiveFactorial(1))

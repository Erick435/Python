function binaryStringExpansion(str, solutions = [], partial = "") {
    const index = str.indexOf("?"); //indexOf returns the first string occurrence of a substring

    if (index < 0) {
        solutions.push(partial + str);
    } else {
        const front = str.slice(0, index); // Returns a section of the string
        const back = str.slice(index + 1); //Returns a section of the string
        const prefix = partial + front; //Slice of a string being processed

        binaryStringExpansion(back, solutions, prefix + "0"); //recursion
        binaryStringExpansion(back, solutions, prefix + "1"); //recursion
    }
    return solutions;
}
console.log(binaryStringExpansion("1?0?")) // ["1000", "1001", "1100", "1101"]
function digitSum(number: number): number {

    // Cool way to capture length of any number
    const length = Math.floor(Math.log10(Math.abs(number))) + 1
    let sum = 0
    let num = number;


    while (num !== 0) {

        const digit = num % 10
        num = Math.floor(num / 10)
        sum += digit

    }

    return sum
}




function reverseNum(number: number): number {

    let reverseNum = 0
    let num = number;


    while (num !== 0) {
        const digit = num % 10
        num = Math.floor(num / 10)

        reverseNum = (reverseNum * 10) + digit

    }

    return reverseNum
}



function isPalidrome(number: number): boolean {

    const numString = number.toString();
    const lastIndex = numString.length -1;

    for (let i = 0; i < lastIndex - i; i++) {
        
        
        const first = numString[i]
        const last = numString[lastIndex - i]

        console.log("Count: " + i);
        console.log(`First: ${first} Last: ${last}`)

        if (first !== last) return false
    }




    return true

}

function isPalidromeEfficient(number: number): boolean {

    const numReverse = reverseNum(number);
    
    return number === numReverse

}


console.log(isPalidromeEfficient(123321))

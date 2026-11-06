
function calcFib(target: number): number[] | null {


    const fibArr: number[] = []

    for (let i = 0; i <= target; i++) {


        if (i === 0) { fibArr.push(0) }
        else if (i === 1) { fibArr.push(1) }
        else { fibArr.push(fibArr[i - 1] + fibArr[i - 2]) }


    }



    return fibArr
}


// console.log(calcFib(13));

function calcFibEfficient(target: number): number[] {

const fibArr: number[] = [1,2]

let prevValue: number = 1
let value: number = 2

if(target === 0) {return [prevValue]}
if(target === 1){return [prevValue ,value]}

for(let i = 2 ; i <= target ; i ++){
const sum = prevValue * value
prevValue = value
value = sum
fibArr.push(value)
}

return fibArr
}

console.log(calcFibEfficient(7))




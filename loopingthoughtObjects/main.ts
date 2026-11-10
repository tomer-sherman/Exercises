try {


    const nutrition = { calories: 250, protein: 12, carbs: 30, fat: 8, sugar: 5 };

    function scale(object: object, mult: number): object {
        const scaledArr = Object.entries(object).map(entry => [entry[0], entry[1] * mult]);
        const scaledObj = Object.fromEntries(scaledArr)
        return scaledObj
    }

    console.log(scale(nutrition, 2))











}
catch (err: any) {
    console.log(err);
}
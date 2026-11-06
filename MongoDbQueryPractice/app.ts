import mongoose from "mongoose";
import { MealModel } from "./model";
(async () => {

    try {
        await mongoose.connect(process.env.MONGODB_URI!);


        // const allMeals = await MealModel.find().exec()


        // console.log(allMeals);


        // const mealsOver500Calories = await MealModel.find
        //     ({ calories: { $gt: 500 } }).exec()


        // console.log(mealsOver500Calories);


        // const mealsUnder300Calories = await MealModel.find
        //     ({ calories: { $lt: 300 } })
        //     .select({ desc: 1, calories: 1, _id: 0 })
        //     .sort({ calories: 1 }).exec()


        // console.log(mealsUnder300Calories);


        // const top3ProteinMeals = await MealModel.find()
        //     .select({ desc: 1, protien: 1, _id: 0 })
        //     .sort({ protien: -1, desc: 1 })
        //     .limit(3).exec()


        // console.log(top3ProteinMeals);


        // const highProteinOrLowCalorieMeals = await MealModel.find
        //     ({ $or: [{ protien: { $gte: 40 } }, { calories: { $lt: 250 } }] })
        //     .select({ desc: 1, calories: 1, protien: 1, _id: 0 })
        //     .sort({ calories: 1 }).exec()


        // console.log(highProteinOrLowCalorieMeals);


        // const selectedMealsByCarbs = await MealModel.find
        //     ({ desc: { $in: ["tuna sandwich", "protein bar", "sushi", "pizza margherita"] } })
        //     .select({ desc: 1, carbs: 1, _id: 0 })
        //     .sort({ carbs: -1 }).exec()


        // console.log(selectedMealsByCarbs);


        // const lowestMealFats = await MealModel.
        //     find({ calories: { $lt: 400 } })
        //     .select({ desc: 1, fats: 1, _id: 0 })
        //     .sort({ fats: 1, desc: 1 }).limit(2).exec();

        // console.log(lowestMealFats);

        // const descWithP = await MealModel.
        //     find({ desc: /^p/ })
        //     .select({ desc: 1, _id: 0 })
        //     .sort({ desc: 1 }).exec();

        // console.log(descWithP);

        // const numOfMealsAbove6 = await MealModel.countDocuments({ protien: { $gt: 30 } });
        // console.log(numOfMealsAbove6);

        // const mealsLoggedAt3 = await MealModel
        //     .find({ createdAt: { $gte: new Date("2026-11-03T00:00:00Z"), $lt: new Date("2026-11-04T00:00:00Z") } })
        //     .select({ desc: 1, createdAt: 1, _id: 0 })
        //     .sort({ createdAt: 1, desc: 1 }).exec();

        // console.log(mealsLoggedAt3);


        function convertDateToUtcRange(date: string) {

            const isValid = RegExp(/^\d{4}-\d{2}-\d{2}$/).test(date);
            if (!isValid) throw new Error("Invalid date input");

            const start = new Date(date);
            const end = new Date(start);
            end.setUTCDate(end.getUTCDate() + 1);

            return { start, end }
        }

        const { start, end } = convertDateToUtcRange("2026-11-05");

        const mealsTimeRange = await MealModel.
            find({ createdAt: { $gte: start, $lt: end } })
            .select({ desc: 1, createdAt: 1, _id: 0 })
            .sort({ createdAt: 1, desc: 1 }).exec()

        console.log(mealsTimeRange);





    }
    catch (err: any) {
        console.log(err);
    }
    finally {
        await mongoose.disconnect()
    }
})();

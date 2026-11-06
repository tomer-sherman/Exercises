import mongoose from "mongoose";
import { MealModel } from "./model";
import { DateTime, DateTimeOptions, IANAZone } from "luxon";
(async () => {

    try {
        await mongoose.connect(process.env.MONGODB_URI!);


        // Wihtout luxon, it matches UTC time gives a range or UTC
        function jsDateRange(date: string) {

            const start = new Date(date);
            const end = new Date(start);
            end.setUTCDate(end.getUTCDate() + 1);

            return { start, end }
        }

        function luxonSingleDateRange(timezone: string, date: string) {

            if (!DateTime.fromISO(date).isValid) throw Error("Invalid date string");
            if (!IANAZone.create(timezone).isValid) throw Error("Invalid time zone");
            const zone = IANAZone.create(timezone);

            const luxonStart = DateTime.fromISO(date, { zone }).startOf("day");
            const end = luxonStart.plus({ days: 1 }).toJSDate()
            const start = luxonStart.toJSDate();

            return { start, end };
        }



        async function logMealsWithGivenDateString(obj: any) {

            const start = obj.start as Date
            const end = obj.end as Date

            const mealsTimeRange = await MealModel.
                find({ createdAt: { $gte: start, $lt: end } })
                .select({ desc: 1, createdAt: 1, _id: 0 })
                .sort({ createdAt: 1, desc: 1 }).exec()

            console.log(mealsTimeRange);


        }

        async function logMealsGroupedByDate(timezone: string) {

            if (!IANAZone.create(timezone).isValid) throw Error("Invalid time zone");



            const meals = await MealModel.aggregate([

                {
                    $group: {
                        _id: { $dateToString: { format: "%Y-%m-%d", date: "$createdAt", timezone } },
                        calories: { $sum: "$calories" },
                        meals: { $sum: 1 }
                    }
                },
                { $project: { date: "$_id", totalCalories: "$calories", meals: "$meals", _id: 0 } },
                { $sort: { date: 1, meals: 1 } }


            ])

            console.log(meals);


        } await logMealsGroupedByDate("Asia/Jerusalem");
    

    }
    catch (err: any) {
        console.log(err);
    }
    finally {
        await mongoose.disconnect()
    }
})();

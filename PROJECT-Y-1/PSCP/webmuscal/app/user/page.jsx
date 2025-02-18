"use client";
import React, {useContext, useEffect, useState } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {calorie_goal,protein_goal,carbohydrate_goal,fat_goal,totalCalories,totalprotein,totalcarbohydrate,totalfat,
      calorie_progress,
      protein_progress,
      carbohydrate_progress,
      fat_progress,
    } = useContext(FoodContext);
    
    const newTotalcalories = calorie_progress
    const newTotalprotein = protein_progress
    const newTotalcarbohydrate = carbohydrate_progress
    const newTotalfat = fat_progress

    const [caloriesC,setcaloriesC] = useState("opacity-0")
    const [proteinC,setproteinC] = useState("opacity-0")
    const [carbohydrateC,setcarbohydrateC] = useState("opacity-0")
    const [fatC,setfatC] = useState("opacity-0")

    return(
        <div className="w-screen h-screen p-3 animate-scale">
            <div className="text-[70px] font-krona-r text-[#ffff]"><span className="text-[#E44545]">Go</span>al</div>
            <div className="w-[100%] h-[100%]">
                <div className="flex justify-center items-center gap-10 mt-[20px]">
                    <div className="flex flex-col justify-center items-center gap-5">
                        <div className="w-[220px] h-[100px] bg-[#073575] rounded-3xl flex justify-center items-center p-2">
                            <div className="bg-[#9FCDFF] translate-x-[-65px] translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Calories</div>
                            <div className="text-[30px] font-inter-r text-[#fff]">{`${calorie_goal} Cal`}</div>
                        </div>
                        <div onMouseMove={()=>(setcaloriesC("opacity-1"))} onMouseOut={()=>(setcaloriesC("opacity-0"))} className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden hover:scale-105 duration-500 ease-in-out"><div style={{ height: `${newTotalcalories}%` }}  className={`bg-bb2 w-full rounded-full`}></div></div>
                        <div className={`${caloriesC} absolute text-[20px] font-inter-r text-[#fff] duration-500 ease-in-out`}>{totalCalories} Cal.</div>
                    </div>
                    <div className="flex justify-center items-center gap-5">
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-65px] text-[#fff]  translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Protein</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${protein_goal} G.`}</div>
                            </div>
                            <div onMouseMove={()=>(setproteinC("opacity-1"))} onMouseOut={()=>(setproteinC("opacity-0"))} className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden hover:scale-105 duration-500 ease-in-out"><div style={{ height: `${newTotalprotein}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                            <div className={`${proteinC} absolute text-[20px] font-inter-r text-[#fff] duration-500 ease-in-out`}>{totalprotein} G.</div>
                        </div>
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-40px] text-[#fff]  translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Carbohydrate</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${carbohydrate_goal} G.`}</div>
                            </div>
                            <div onMouseMove={()=>(setcarbohydrateC("opacity-1"))} onMouseOut={()=>(setcarbohydrateC("opacity-0"))} className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden hover:scale-105 duration-500 ease-in-out"><div style={{ height: `${newTotalcarbohydrate}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                            <div className={`${carbohydrateC} absolute text-[20px] font-inter-r text-[#fff] duration-500 ease-in-out`}>{totalcarbohydrate} G.</div>
                        </div>
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-75px] text-[#fff] translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Fat</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${fat_goal} G.`}</div>
                            </div>
                            <div onMouseMove={()=>(setfatC("opacity-1"))} onMouseOut={()=>(setfatC("opacity-0"))} className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden hover:scale-105 duration-500 ease-in-out"><div style={{ height: `${newTotalfat}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                            <div className={`${fatC} absolute text-[20px] font-inter-r text-[#fff] duration-500 ease-in-out`}>{totalfat} G.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Page;
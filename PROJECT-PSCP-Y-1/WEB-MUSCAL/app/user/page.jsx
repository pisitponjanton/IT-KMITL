"use client";
import React, {useContext, useEffect } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {calories,protein,carbohydrate,fat,totalCalories,totalprotein,totalcarbohydrate,totalfat} = useContext(FoodContext);
    const newTotalcalories = (totalCalories / calories) * 100;
    const newTotalprotein = (totalprotein / protein) * 100;
    const newTotalcarbohydrate = (totalcarbohydrate / carbohydrate) * 100;
    const newTotalfat = (totalfat / fat) * 100;
    return(
        <div className="w-screen h-screen p-3 animate-scale">
            <div className="text-[70px] font-krona-r text-[#ffff]"><span className="text-[#E44545]">Go</span>al</div>
            <div className="w-[100%] h-[100%]">
                <div className="flex justify-center items-center gap-10 mt-[20px]">
                    <div className="flex flex-col justify-center items-center gap-5">
                        <div className="w-[220px] h-[100px] bg-[#073575] rounded-3xl flex justify-center items-center p-2">
                            <div className="bg-[#9FCDFF] translate-x-[-65px] translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Calories</div>
                            <div className="text-[30px] font-inter-r text-[#fff]">{`${calories} Cal`}</div>
                        </div>
                        <div className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden"><div style={{ height: `${newTotalcalories}%` }}  className={`bg-bb2 w-full rounded-full`}></div></div>
                    </div>
                    <div className="flex justify-center items-center gap-5">
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-65px] text-[#fff]  translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Protein</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${protein} G.`}</div>
                            </div>
                            <div className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden"><div style={{ height: `${newTotalprotein}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                        </div>
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-40px] text-[#fff]  translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Carbohydrate</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${carbohydrate} G.`}</div>
                            </div>
                            <div className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden"><div style={{ height: `${newTotalcarbohydrate}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                        </div>
                        <div className="flex flex-col justify-center items-center gap-5">
                            <div className="w-[220px] h-[100px] bg-[#102A46] rounded-3xl flex justify-center items-center p-2">
                                <div className="translate-x-[-75px] text-[#fff] translate-y-[-30px] w-[70px] h-[20px] absolute rounded-2xl flex justify-center items-center font-inter-r">Fat</div>
                                <div className="text-[30px] font-inter-r text-[#fff]">{`${fat} G.`}</div>
                            </div>
                            <div className="w-[150px] h-[60vh] bg-[#D9D9D9]/30  rounded-full overflow-hidden"><div style={{ height: `${newTotalfat}%` }} className="bg-bb2 w-full rounded-full"></div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Page;
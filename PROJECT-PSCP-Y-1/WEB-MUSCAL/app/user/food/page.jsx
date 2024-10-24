"use client";
import Link from "next/link";
import React, {useContext } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {foodList} = useContext(FoodContext);
    return(
        <div className="w-screen h-screen flex flex-col p-[20px] animate-scale1">
            <div className="font-krona-r text-[#E44545] text-[60px]">Food <span className="text-[#ffff]">Log</span></div>
            <div className="flex items-center">
                <Link href="/user/food/addfood">
                    <div className="bg-bb1 flex items-center p-1 rounded-2xl pr-4 pl-4 hover:scale-105 duration-500 ease-in-out cursor-pointer gap-1">
                        <div className="text-[25px] text-[#ffff] font-inter-r text-center">Add food</div>
                        <div className="bg-cl hover:bg-p duration-500 ease-in-out bg-cover bg-center w-[50px] h-[50px]"></div>
                    </div>
                </Link>
            </div>
            <div className="flex gap-5 flex-col items-center w-full h-full overflow-scroll">
                <div className="w-[800px] h-full mt-[40px]">
                {foodList.map((food, index) => (
                        <div
                        key={index}
                        className="w-full h-[120px] flex justify-around items-center rounded-3xl bg-[#031420] m-5 p-5">
                            <div className="font-inter-r text-[#FFFFFF] text-[40px]">{food.name}</div>
                            <div className="text-[#858585] text-[20px] font-inter-r">{`${food.calories} cal, ${food.protein} g, ${food.carbohydrate} g, ${food.fat} g`}</div>
                        </div>
                ))}
                </div>
            </div>
        </div>
    )
}
export default Page;
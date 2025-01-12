'use client';

import { useState } from "react";
import React, {useContext } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {foodList,
        foodadd,
        setfood_name,
        setserving_size,
        setservings_per_container,
        setcalories_per_serving,
        setcarbohydrates_per_serving,
        setprotein_per_serving,
        setfat_per_serving,
        logfood,
    } = useContext(FoodContext);
    // const [van,setvan] = useState("translate-x-[250px]")
    const [cc,setcc] = useState("opacity-0 z-[-10]")
    const [bgc,setbgc] = useState("bg-[#FFFFFF] text-[#1A4472]")

    return(
        <div className="w-screen h-screen flex flex-col gap-2 p-[20px]">
            <div className="font-krona-r text-[#E44545] text-[60px]">Add <span className="text-[#ffff]">Food</span></div>
            {/* <div className="flex items-center">
                <input onFocus={(e)=>{(e)=setvan("translate-x-[450px]")}} onBlur={(e)=>{(e)=setvan("translate-x-[250px]")}} className="w-[300px] h-[70px] p-5 bg-bb1 rounded-2xl text-[20px] duration-300 ease-in-out focus:w-[500px] outline-none text-[#fff]" placeholder="Enter menu"/>
                <div className={`${van} hover:scale-105 duration-300 ease-in-out absolute bg-van bg-cover bg-center w-[36px] h-[36px]`}></div>
            </div> */}
            <div onClick={(e)=>(e)=(setcc(ee => ee === "opacity-0 z-[-10]" ? "opacity-1": "opacity-0 z-[-10]"),setbgc(ee => ee === "bg-[#FFFFFF] text-[#1A4472]" ? "bg-bb3 text-[#ffff]": "bg-[#FFFFFF] text-[#1A4472]"))} className={`w-[250px] h-[65px] ${bgc} cursor-pointer p-5 mt-3 hover:text-[#ffff] hover:bg-bb3 rounded-2xl flex justify-center items-center`}>
                <div className="text-[25px] font-inter-r">Create meal</div>
            </div>
            <div className={`w-[500px] h-[565px] gap-4 translate-x-[200px] flex flex-col duration-300 ease-in-out rounded-2xl translate-y-[185px] ${cc} absolute bg-[#102A46]`}>
                <form className="flex flex-col p-5 gap-4" onSubmit={foodadd}>
                    <input type="text" onChange={(e)=>(setfood_name(e.target.value))} className="bg-[#999999] focus:w-[300px] duration-300 ease-in-out w-[200px] text-[#fff] text-[18px] h-[50px] outline-none p-3 rounded-xl placeholder:text-[#fff] " placeholder="Enter Foodname"/>
                    <input type="number" onChange={(e)=>(setserving_size(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear text-[#fff]" placeholder="Enter serving size"/>
                    <input type="number" onChange={(e)=>(setservings_per_container(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear text-[#fff]" placeholder="Enter serving per"/>
                    <input type="number" onChange={(e)=>(setcalories_per_serving(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear text-[#fff]" placeholder="Enter Calories"/>
                    <input type="number" onChange={(e)=>(setprotein_per_serving(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear  text-[#fff]" placeholder="Enter Protein"/>
                    <input type="number" onChange={(e)=>(setcarbohydrates_per_serving(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear  text-[#fff]" placeholder="Enter Carbohydrates"/>
                    <input type="number" onChange={(e)=>(setfat_per_serving(e.target.value))} className="w-[250px] h-[50px] outline-none text-[20px] bg-[#D9D9D9] p-5 rounded-2xl focus:w-[400px] duration-100 ease-linear  text-[#fff]" placeholder="Enter Fat"/>
                    <button type="submit" onClick={()=>(setcc("opacity-0 z-[-10]"))} className="text-[#fff] bg-bb rounded-2xl text-[20px] hover:scale-105 duration-300 ease-in-out p-5">Enter</button>
                </form>
            </div>
            <div className="text-[30px] font-inter-r text-[#ffff]">My food</div>
            <div className="w-full h-full flex flex-col justify-center items-center overflow-scroll">
                <div className="w-[800px] h-full mt-[40px]">
                {foodList.map((food, index) => (
                    <div key={index} className="w-full h-[120px] flex justify-around items-center rounded-3xl bg-[#031420] m-5 p-5">
                        <div className="font-inter-r text-[#FFFFFF] text-[40px]">{food.food_name}</div>
                        <div className="text-[#858585] text-[20px] font-inter-r">
                            {`${food.nutritions.calories_per_serving} cal, ${food.nutritions.protein_per_serving} g, ${food.nutritions.carbohydrates_per_serving} g, ${food.nutritions.fat_per_serving} g`}
                        </div>
                        <div onClick={()=> logfood(food.food_id,1)} className=" cursor-pointer hover:scale-110 duration-300 ease-in-out text-[15px] bg-white p-3 rounded-2xl">add</div>
                    </div>
                ))}
                </div>
            </div>
        </div>
    )
}
export default Page;
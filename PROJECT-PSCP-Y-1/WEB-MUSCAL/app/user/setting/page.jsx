'use client';
import Link from "next/link";
import { useState } from "react";
import React, {useContext } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {setcalories,setprotein,setcarbohydrate,setfat} = useContext(FoodContext);
    const [box,setbox] =useState('hidden')
    const [username,setusername] = useState('')
    const [password,setpassword] = useState('hidden')
    const [n,setn] = useState("Change password")
    const [ci,setci] = useState(0)
    const [hh,sethh] =useState("")
    const [hh1,sethh1] =useState("hidden")
    const cc=()=>{
        setusername("hidden");
        setpassword("");
        setn("Next");
        if(ci===1){
            sethh("hidden")
            sethh1("")
        }
        setci(1)
    }
    return(
        <div className=" w-screen h-screen flex flex-col p-5 mt-[20px]">
            <div className="flex justify-center gap-10 items-center">
                <div onClick={()=>(setbox("hidden"))} className=" hover:scale-110 duration-500 ease-in-out w-[250px] cursor-pointer h-[60px] rounded-3xl bg-[#073575] flex justify-center items-center text-[#fff] text-[25px] font-inter-r"><div>Edit Account</div></div>
                <div onClick={()=>(setbox(ee=>ee==="z-[20]" ? "hidden" :"z-[20]" ))} className=" hover:scale-110 duration-500 ease-in-out w-[250px] cursor-pointer h-[60px] rounded-3xl bg-[#073575] flex justify-center items-center text-[#fff] text-[25px] font-inter-r"><div>Edit Goal</div></div>
                <Link href="/" className="hover:scale-110 duration-500 ease-in-out cursor-pointer">
                    <div className="w-[250px] h-[60px] rounded-3xl bg-[#FFFFFF] flex justify-center items-center text-[#FF0000] text-[25px] font-inter-r"><div>Log Out</div></div>
                </Link>
            </div>
            <div className="flex flex-col justify-center translate-y-[280px] translate-x-[80px] gap-[20px]">
                <form className="flex flex-col justify-center gap-[20px]">
                    <div className={`${hh}`}>
                        <div className={`flex flex-col gap-2 ${username}`}>
                            <div className="text-[20px] text-[#fff]">Username</div>
                            <div className="ml-4 w-[500px] h-[50px] text-[#8E8E8E] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3">Jacob Nig</div>
                        </div>
                        <div className="flex flex-col gap-2">
                            <div className="text-[20px] text-[#fff]">Password</div>
                            <div className={`ml-4 w-[500px] h-[50px] text-[#8E8E8E] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3 ${username}`}>*********</div>
                            <input type="password" className={`ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3 ${password}`} placeholder="*********"></input>
                        </div>
                    </div>
                    <div className={`${hh1}`}>
                        <div className={`flex flex-col gap-2`}>
                            <div className="text-[20px] text-[#fff]">New password</div>
                            <input type="password" className="ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3" placeholder="*********"></input>
                        </div>
                        <div className="flex flex-col gap-2">
                            <div className="text-[20px] text-[#fff]">Confirm password</div>
                            <input type="password" className={`ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3`} placeholder="*********"></input>
                        </div>
                    </div>
                    <div onClick={cc} className={`${hh} hover:scale-105 duration-300 ease-in-out cursor-pointer flex justify-center items-center relative left-[15px] w-[180px] text-[#ffff] h-[30px] p-5 rounded-2xl bg-[#1A4472]`}><div>{n}</div></div>
                    <button type="submit" className=" hover:scale-105 duration-300 ease-in-out cursor-pointer flex justify-center items-center relative left-[340px] w-[180px] text-[#1A4472] h-[30px] p-5 rounded-2xl bg-[#ffff] text-[20px]"><div>Save change</div></button>
                </form>
            </div>
            <div className={`${box} w-[45vw] gap-5 h-[80vh] translate-y-[90px] translate-x-[200px] duration-300 ease-in-out bg-bb opacity-95 absolute rounded-3xl flex flex-col p-10`}>
                <form onSubmit={(e)=>(e.preventDefault())}>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Calories</div>
                        <input type="number" onChange={(e)=>(setcalories(e.target.value))} min={0} max={50000} placeholder="Goal Calories 0-50,000 Cal." className=" text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6] text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Protein</div>
                        <input type="number" onChange={(e)=>(setprotein(e.target.value))} min={0} max={50000} placeholder="Goal Protein 0-125 G." className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Carbohydrate</div>
                        <input type="number" onChange={(e)=>(setcarbohydrate(e.target.value))}  min={0} max={50000} placeholder="Goal Carbohydrate 0-250 G." className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Fat</div>
                        <input type="number" onChange={(e)=>(setfat(e.target.value))}  min={0} max={50000} placeholder="Goal Fat 0-60 G." className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <input type="submit" className=" hidden"></input>
                </form>
            </div>
        </div>
    )
}
export default Page;
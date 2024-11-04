'use client';

import {useState } from "react";
import React, {useContext } from 'react';
import FoodContext from "@/app/context";
const Page=()=>{
    const {setcalories,setprotein,setcarbohydrate,setfat,name2,tt,
        setgoal
    } = useContext(FoodContext);
    const [box,setbox] =useState('hidden')
    const [username,setusername] = useState('')
    const [password,setpassword] = useState('hidden')
    const [n,setn] = useState("Change password")
    const [ci,setci] = useState(0)
    const [hh,sethh] =useState("")
    const [hh1,sethh1] =useState("hidden")

    const [npassword,setnpassword] = useState("")

    const [newpassword,setnewpassword] = useState("")
    const [conpassword,setconpassword] = useState("")

    const cp=()=>{
        if(newpassword === conpassword && newpassword && conpassword && ci){
            tt[name2]=newpassword
            setusername("");
            setpassword("hidden");
            setn("Change password");
            sethh("")
            sethh1("hidden")
            setci(0)
            alert("The password has been changed.")
        }else if(ci==2){
            alert("Passwords != ConfirmPassword")
        }
    }
    const cc=()=>{
        setusername("hidden");
        setpassword("");
        setn("Next");
        if(ci===1){
            if(npassword==tt[name2]){
                sethh("hidden")
                sethh1("")
            }else{
                alert("The system is under development.")
            }
            setci(2)
        }
        setci(1)
    }
    const logout =()=>{
        localStorage.setItem('position', '')
        localStorage.setItem('Authorization', '')
        window.location.href = "/"
    }
    return(
        <div className=" w-screen h-screen flex flex-col p-5 mt-[20px]">
            <div className="flex justify-center gap-10 items-center">
                <div onClick={()=>(setbox("hidden"))} className=" hover:scale-110 duration-500 ease-in-out w-[250px] cursor-pointer h-[60px] rounded-3xl bg-[#073575] flex justify-center items-center text-[#fff] text-[25px] font-inter-r"><div>Edit Account</div></div>
                <div onClick={()=>(setbox(ee=>ee==="z-[20]" ? "hidden" :"z-[20]" ))} className=" hover:scale-110 duration-500 ease-in-out w-[250px] cursor-pointer h-[60px] rounded-3xl bg-[#073575] flex justify-center items-center text-[#fff] text-[25px] font-inter-r"><div>Edit Goal</div></div>
                <div onClick={logout} className="hover:scale-110 duration-500 ease-in-out cursor-pointer">
                    <div className="w-[250px] h-[60px] rounded-3xl bg-[#FFFFFF] flex justify-center items-center text-[#FF0000] text-[25px] font-inter-r"><div>Log Out</div></div>
                </div>
            </div>
            <div className="flex flex-col justify-center translate-y-[280px] translate-x-[80px] gap-[20px]">
                <div className="flex flex-col justify-center gap-[20px]">
                    <div className={`${hh}`}>
                        <div className={`flex flex-col gap-2 ${username}`}>
                            <div className="text-[20px] text-[#fff]">Username</div>
                            <div className="ml-4 w-[500px] h-[50px] text-[#8E8E8E] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3">{name2}</div>
                        </div>
                        <div className="flex flex-col gap-2">
                            <div className="text-[20px] text-[#fff]">Password</div>
                            <div className={`ml-4 w-[500px] h-[50px] text-[#8E8E8E] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3 ${username}`}>*********</div>
                            <input onChange={(e)=>(setnpassword(e.target.value))} type="password" className={`ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3 ${password}`} placeholder="*********"></input>
                        </div>
                    </div>
                    <div className={`${hh1}`}>
                        <div className={`flex flex-col gap-2`}>
                            <div className="text-[20px] text-[#fff]">New password</div>
                            <input onChange={(e)=>(setnewpassword(e.target.value))} type="password" className="ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3" placeholder="*********"></input>
                        </div>
                        <div className="flex flex-col gap-2">
                            <div className="text-[20px] text-[#fff]">Confirm password</div>
                            <input onChange={(e)=>(setconpassword(e.target.value))} type="password" className={`ml-4 w-[500px] h-[50px] text-[#ffff] bg-[#D9D9D9] bg-opacity-0 border-[0.1px] outline-none p-3`} placeholder="*********"></input>
                        </div>
                    </div>
                    <div onClick={cc} className={`${hh} hover:scale-105 duration-300 ease-in-out cursor-pointer flex justify-center items-center relative left-[15px] w-[180px] text-[#ffff] h-[30px] p-5 rounded-2xl bg-[#1A4472]`}><div>{n}</div></div>
                    <button onClick={cp} type="submit" className=" hover:scale-105 duration-300 ease-in-out cursor-pointer flex justify-center items-center relative left-[340px] w-[180px] text-[#1A4472] h-[30px] p-5 rounded-2xl bg-[#ffff] text-[20px]"><div>Save change</div></button>
                </div>
            </div>
            <div className={`${box} w-[45vw] gap-5 h-[80vh] translate-y-[90px] translate-x-[200px] duration-300 ease-in-out bg-bb opacity-95 absolute rounded-3xl flex flex-col p-10`}>
                <form onSubmit={(e)=>{e.preventDefault(),setgoal(),setbox('hidden')}}>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Calories</div>
                        <input type="number" onChange={(e)=>(setcalories(Math.ceil(e.target.value)))} min={0} max={100000} placeholder="Goal Calories 0-50,000 Cal." className=" text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6] text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Protein</div>
                        <input type="number" onChange={(e)=>(setprotein(Math.ceil(e.target.value)))} min={0} max={100} placeholder="Protein target 0-100% of target calories" className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Carbohydrate</div>
                        <input type="number" onChange={(e)=>(setcarbohydrate(Math.ceil(e.target.value)))}  min={0} max={100} placeholder="Goal Carbohydrate 0-100% of target calories" className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex flex-col">
                        <div className="text-[#ffff] text-[40px]">Goal Fat</div>
                        <input type="number" onChange={(e)=>(setfat(Math.ceil(e.target.value)))}  min={0} max={100} placeholder="Goal Fat 0-100% of target calories" className="text-[#fff] placeholder:text-[#ffff] ml-8 w-[500px] h-[60px] bg-[#A6A6A6]  text-[20px] outline-none rounded-2xl p-5"/>
                    </div>
                    <div className="flex justify-center items-center w-[100%] mt-[40px]">
                        <button type="submit" className="text-[#ffff] text-[30px]">Edit Goal</button>
                    </div>
                </form>
            </div>
        </div>
    )
}
export default Page;
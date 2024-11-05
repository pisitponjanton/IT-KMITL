"use client";

import { useState,useContext, useEffect } from "react";
import FoodContext from "./context";

export default function Page() {
  const {tt,login1,setusername,setpassword,hh,sethh,setccpassword,register1

  } = useContext(FoodContext)
  const [ac,setac] = useState('')
  const [num1,setnum1] = useState(0)
  const [login,setlogin] = useState("")
  const [bgi,setbgi] = useState("bg-img2")
  const [register,setregister] = useState("translate-x-[100vw]")
  const [am,setam] = useState("")

  const ani=()=>{
      setam("animate-spin")
  }
  const ani1=()=>{
    setam("")
  }

  const c1=()=>{
    if (num1==0){
      setnum1(1)
      setac("translate-x-[50vw]")
      setlogin("translate-x-[-100vw]")
      setregister("")
      setbgi("bg-img1")
    }
    else{
      setnum1(0)
      setac("")
      setlogin("")
      setregister("translate-x-[100vw]")
      setbgi("bg-img2")
    }
  }


  useEffect(()=>{
    if(localStorage.getItem('position')){
      window.location.href='/user'
    }
  })

  return (
      <div className="bg-[#031420] w-screen h-screen overflow-hidden flex items-center">
          <div className={` h-[100vh] w-[100vw] ${bgi} duration-500 ease-in-out bg-cover bg-center bg-no-repeat`}>
            <div className=" flex flex-col justify-center items-center translate-x-[27vw] translate-y-[60px] gap-[15px]">
              <div className={`bg-c3 bg-cover bg-center bg-no-repeat w-[360px] h-[350px] hover:animate-spin animate-sp1 ${am}`}></div>
              <div className={`bg-c3_2 bg-cover bg-center bg-no-repeat w-[360px] h-[350px] hover:animate-spin animate-sp1 ${am}`}></div>
            </div>
            <div className="absolute translate-y-[-605px] translate-x-[11vw]">
              <div className="hover:animate-spin animate-sp1 bg-c4 bg-cover bg-center bg-no-repeat w-[464.99px] h-[425.59px]"></div>
            </div>
          </div>
          <div className={`${hh} duration-500 ease-in-out absolute w-screen h-screen flex justify-center items-center z-10`}>
            <div className=" rounded-3xl text-[#ffff] flex flex-col justify-center items-center bg-bb w-[300px] h-[150px]">
              <div>Username or password is incorrect.</div>
              <div onClick={()=>(sethh("translate-x-[-100vw]"))} className=" translate-y-[15px] bg-white text-black px-[10px] rounded-lg cursor-pointer">OK</div>
            </div>
          </div>
          <div className={`${ac} duration-500 ease-in-out overflow-hidden absolute w-[50vw] h-[100vh] bg-[#A8DADC] bg-opacity-30 backdrop-blur-xl`}>
            <div className={`flex flex-col items-center`}>
              <div className="bg-icon bg-cover bg-center bg-no-repeat w-[420px] h-[120px] mt-[90px]"></div>
              <div className={`flex flex-col items-center ${login} absolute translate-y-[200px] duration-500 ease-in-out`}>
                <div className="font-inter-r text-[#FFFFFF] text-[40px] text-stroke mt-[80px]">Login to Your Account</div>
                <div className="flex flex-col justify-center font-inter-r gap-2 mt-[20px]">
                  <div className="text-[#FFFFFF] text-stroke text-[20px]">Username</div>
                  <input type="text" onChange={(e)=>(setusername(e.target.value))} Placeholder="Enter user name" className="text-[#ADACAC] text-stroke rounded-2xl w-[400px] p-3 bg-[#1B0C1A] bg-opacity-50 outline-none"/>
                </div>
                <div className="flex flex-col justify-center font-inter-r gap-2 mt-[20px]">
                  <div className="text-[#FFFFFF] text-stroke text-[20px]">Password</div>
                  <input type="password" onChange={(e)=>(setpassword(e.target.value))} Placeholder="Enter password" className="text-[#ADACAC] text-stroke rounded-2xl w-[400px] p-3 bg-[#1B0C1A] bg-opacity-50 outline-none"/>
                </div>
                <button onClick={login1} onMouseMove={ani} onMouseOut={ani1} className=" hover:scale-105 duration-300 ease-in-out w-[100px] mt-[40px] rounded-xl text-stroke text-[#FFFFFF] h-[50px] bg-[#6D1F2A]">Login</button>
                <div onClick={c1} className=" cursor-pointer text-stroke text-[#FFFFFF] mt-[20px]">Create an acount</div>
              </div>
              <div className={`flex flex-col items-center ${register} absolute translate-y-[200px] duration-500 ease-in-out`}>
                <div className="font-inter-r text-[#FFFFFF] text-[40px] text-stroke mt-[40px]">Create your account</div>
                <div className="flex flex-col justify-center font-inter-r gap-2 mt-[20px]">
                  <div className="text-[#FFFFFF] text-stroke text-[20px]">Username</div>
                  <input onChange={(e)=>(setusername(e.target.value))} type="text" Placeholder="Enter user name" className="text-[#ADACAC] text-stroke rounded-2xl w-[400px] p-3 bg-[#1B0C1A] bg-opacity-50 outline-none"/>
                </div>
                <div className="flex flex-col justify-center font-inter-r gap-2 mt-[20px]">
                  <div className="text-[#FFFFFF] text-stroke text-[20px]">Password</div>
                  <input onChange={(e)=>(setpassword(e.target.value))} type="password" Placeholder="Enter password" className="text-[#ADACAC] text-stroke rounded-2xl w-[400px] p-3 bg-[#1B0C1A] bg-opacity-50 outline-none"/>
                </div>
                <div className="flex flex-col justify-center font-inter-r gap-2 mt-[20px]">
                  <div className="text-[#FFFFFF] text-stroke text-[20px]">Confirm password</div>
                  <input onChange={(e)=>(setccpassword(e.target.value))} type="password" Placeholder="Enter Confirm password" className="text-[#ADACAC] text-stroke rounded-2xl w-[400px] p-3 bg-[#1B0C1A] bg-opacity-50 outline-none"/>
                </div>
                <button onClick={register1} type="submit" className=" hover:scale-105 duration-300 ease-in-out w-[150px] mt-[40px] rounded-xl text-stroke text-[#FFFFFF] h-[50px] bg-[#102A46]">Create an acount</button>
                <div onClick={c1} className=" cursor-pointer text-stroke text-[#FFFFFF] mt-[20px]">Login acount</div>
              </div>
            </div>
          </div>
      </div>
  );
}

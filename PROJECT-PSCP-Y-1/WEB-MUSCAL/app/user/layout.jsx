"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect,useState } from "react";

export default function RootLayout({ children }) {
  const pname = usePathname()
  const [wh,setwh] = useState('translate-y-[-80px]')
  const [day,setday] = useState("")
  const [pro,setpro] = useState("hidden")
  const [prof,setprof] = useState("bg-bb")
  const [name,setname] = useState("text-[20px]")
  useEffect(()=>{
    if(pname == "/user"){
      setwh("translate-y-[-80px]")
      setday("")
      setpro("hidden")
      setprof("bg-bb")
      setname("text-[20px]")
    }else if(pname == "/user/food"|| pname == "/user/food/addfood" ){
      setwh("translate-y-[0px]")
      setday("")
      setpro("hidden")
      setprof("bg-bb")
      setname("text-[20px]")
    }else if(pname == "/user/setting"){
      setwh("translate-y-[80px]")
      setday("opacity-0 z-[-1] absolute")
      setpro("")
      setprof("absolute translate-x-[350px] translate-y-[40px]")
      setname("absolute translate-x-[220px] translate-y-[50px] text-[40px]")
    }
  },[pname])
  return (
    <html lang="en">
      <body>
        <div className=" flex items-center overflow-hidden w-screen h-screen bg-img11 bg-cover bg-center bg-no-repeat">
            <div className=" h-screen z-10">
              <div className={`${prof} duration-500 ease-in-out mt-5 w-[300px] h-[350px] rounded-e-2xl flex flex-col gap-10 justify-center items-center`}>
                <div className=" w-[200px] h-[200px] bg-white hover:scale-105 duration-500 ease-linear cursor-pointer rounded-full"></div>
                <div className={`text-[#FFFFFF] font-inter-r ${name} duration-500 ease-in-out`}>Jacob Nig</div>
              </div>
              <div className={`${pro} p-5`}>
                <div className="font-krona-r text-[#E44545] text-[60px]">Set<span className="text-[#ffff]">ting</span></div>
              </div>
              <div className="mt-5 flex flex-col justify-center items-center">
                <div className={`${day} w-[200px] h-[50px] flex justify-center gap-5 items-center bg-bb1 rounded-2xl`}>
                  <div className=" text-[#FFFFFF] font-inter-r text-[20px]">D / M / Y</div>
                  <div className="w-[16px] h-[8px] bg-dod bg-cover bg-center"></div>
                </div>
                <div className="mt-10 flex flex-col justify-center items-center">
                  <div className={`${wh} duration-500 ease-in-out absolute rounded-full w-[250px] h-[80px] bg-[#7A212F]`}></div>
                  <Link href='/user' className="z-[2]">
                    <div className=" cursor-pointer flex items-center pl-[30px] gap-[15px] w-[250px] h-[80px]">
                      <div className="bg-l bg-cover bg-center w-[60px] h-[60px]"></div>
                      <div className="text-[#FFFFFF] font-inter-r text-[20px]">Goal</div>
                    </div>
                  </Link>
                  <Link href='/user/food' className="z-[2]">
                    <div className=" cursor-pointer flex items-center pl-[30px] gap-[15px] w-[250px] h-[80px]">
                      <div className="bg-food bg-cover bg-center w-[50px] h-[50px]"></div>
                      <div className="text-[#FFFFFF] font-inter-r text-[20px]">Food log</div>
                    </div>
                  </Link>
                  <Link href='/user/setting' className="z-[2]">
                    <div className=" cursor-pointer flex items-center pl-[30px] gap-[15px] w-[250px] h-[80px]">
                      <div className="bg-set bg-cover bg-center w-[60px] h-[60px]"></div>
                      <div className="text-[#FFFFFF] font-inter-r text-[20px]">Setting</div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
            {children}
        </div>
      </body>
    </html>
  );
}

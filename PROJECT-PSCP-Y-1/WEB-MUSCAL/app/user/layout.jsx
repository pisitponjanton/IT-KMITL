"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect,useState } from "react";

export default function RootLayout({ children }) {
  const pname = usePathname()
  const [wh,setwh] = useState('translate-y-[-80px]')
  useEffect(()=>{
    if(pname == "/user"){
      setwh("translate-y-[-80px]")
    }else if(pname == "/user/food"){
      setwh("translate-y-[0px]")
    }else if(pname == "/user/setting"){
      setwh("translate-y-[80px]")
    }
  },[pname])
  return (
    <html lang="en">
      <body>
        <div className="flex items-center overflow-hidden w-screen h-screen bg-img11 bg-cover bg-center bg-no-repeat">
            <div className=" h-screen">
              <div className="mt-5 w-[300px] h-[350px] rounded-e-2xl bg-bb flex flex-col gap-10 justify-center items-center">
                <div className=" w-[200px] h-[200px] bg-white hover:scale-105 duration-300 ease-linear cursor-pointer rounded-full"></div>
                <div className="text-[#FFFFFF] font-inter-r text-[20px]">Jacob Nig</div>
              </div>
              <div className="mt-5 flex flex-col justify-center items-center">
                <div className="w-[200px] h-[50px] flex justify-center gap-5 items-center bg-bb1 rounded-2xl">
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

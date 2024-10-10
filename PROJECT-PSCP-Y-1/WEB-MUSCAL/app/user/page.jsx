"use client";

import { useState } from "react";

const Page=()=>{
    const [f1,setf1] = useState("text-[18px]")
    const [t1,sett1] = useState("")
    const [i1,seti1] = useState("hidden")
    const [h1,seth1] = useState("")

    const [v1,setv1] = useState("add goal calories")
    const handleChange1=(e) => {
        setv1(`${e.target.value} Cal`)
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if(v1!=="add goal calories"){
            seth1(""); 
            seti1("hidden");
            sett1("hidden")
            setf1('text-[30px] mt-[8px]')
        }
    };
    
    return(
        <div className="w-screen h-screen flex flex-col p-[20px]">
            <div className="text-[#E44545] text-[60px] font-krona-r drop-shadow-2xl">Go<span className="text-[#FFFFFF]">al</span></div>
            <div className=" w-[75vw] h-screen flex justify-around">
                <div className="flex flex-col items-center gap-5">
                    <div className="bg-[#073575] shadow-inner rounded-3xl w-[220px] h-[110px] p-5 flex items-center justify-center">
                        <div className="flex flex-col justify-center items-center">
                            <div className="bg-[#9FCDFF] p-1 pl-2 pr-2 rounded-2xl font-inter-r text-center">Calories</div>
                            <div className={`text-center text-[#ffff] font-inter-r ${f1} `}>{v1}</div>
                        </div>
                        <div className={`flex justify-center items-center ${t1}`}>
                            <div onClick={() => {seth1("hidden"); seti1("");}} className={`${h1} bg-p w-[50px] h-[50px] bg-cover bg-center hover:scale-105 duration-500 ease-in-out cursor-pointer`}></div>
                            <div className={`${i1} bg-[#073575] w-[130px] h-[60px] flex justify-center items-center rounded-3xl translate-x-[40px]`}>
                                <form onSubmit={handleSubmit}>
                                    <input className={` w-[120px] h-[50px] bg-[#B0D1FF] flex items-center rounded-2xl outline-none p-2 caret-white text-[20px] text-black number-input`} type="number" min="0" max="5000" onChange={handleChange1}></input>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div className="w-[125px] h-[550px] flex justify-center rounded-full bg-[#D9D9D9]/30 overflow-hidden">
                        <div className={`w-[130px] h-[140px] bg-bb2 rounded-full`}></div>
                    </div>
                </div>
                <div className="flex flex-col items-center gap-5">
                    <div className="bg-[#073575] shadow-inner rounded-3xl w-[220px] h-[110px] p-5 flex items-center justify-center">
                        <div className="flex flex-col justify-center items-center">
                            <div className="bg-[#9FCDFF] p-1 pl-2 pr-2 rounded-2xl font-inter-r text-center">Calories</div>
                            <div className={`text-center text-[#ffff] font-inter-r ${f1} `}>{v1}</div>
                        </div>
                        <div className={`flex justify-center items-center ${t1}`}>
                            <div onClick={() => {seth1("hidden"); seti1("");}} className={`${h1} bg-p w-[50px] h-[50px] bg-cover bg-center hover:scale-105 duration-500 ease-in-out cursor-pointer`}></div>
                            <div className={`${i1} bg-[#073575] w-[130px] h-[60px] flex justify-center items-center rounded-3xl translate-x-[40px]`}>
                                <form onSubmit={handleSubmit}>
                                    <input className={` w-[120px] h-[50px] bg-[#B0D1FF] flex items-center rounded-2xl outline-none p-2 caret-white text-[20px] text-black number-input`} type="number" min="0" max="5000" onChange={handleChange1}></input>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div className="w-[125px] h-[550px] flex justify-center rounded-full bg-[#D9D9D9]/30 overflow-hidden">
                        <div className={`w-[130px] h-[200px] bg-bb2 rounded-full`}></div>
                    </div>
                </div>
                <div className="flex flex-col items-center gap-5">
                    <div className="bg-[#073575] shadow-inner rounded-3xl w-[220px] h-[110px] p-5 flex items-center justify-center">
                        <div className="flex flex-col justify-center items-center">
                            <div className="bg-[#9FCDFF] p-1 pl-2 pr-2 rounded-2xl font-inter-r text-center">Calories</div>
                            <div className={`text-center text-[#ffff] font-inter-r ${f1} `}>{v1}</div>
                        </div>
                        <div className={`flex justify-center items-center ${t1}`}>
                            <div onClick={() => {seth1("hidden"); seti1("");}} className={`${h1} bg-p w-[50px] h-[50px] bg-cover bg-center hover:scale-105 duration-500 ease-in-out cursor-pointer`}></div>
                            <div className={`${i1} bg-[#073575] w-[130px] h-[60px] flex justify-center items-center rounded-3xl translate-x-[40px]`}>
                                <form onSubmit={handleSubmit}>
                                    <input className={` w-[120px] h-[50px] bg-[#B0D1FF] flex items-center rounded-2xl outline-none p-2 caret-white text-[20px] text-black number-input`} type="number" min="0" max="5000" onChange={handleChange1}></input>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div className="w-[125px] h-[550px] flex justify-center rounded-full bg-[#D9D9D9]/30 overflow-hidden">
                        <div className={`w-[130px] h-[300px] bg-bb2 rounded-full`}></div>
                    </div>
                </div>
                <div className="flex flex-col items-center gap-5">
                    <div className="bg-[#073575] shadow-inner rounded-3xl w-[220px] h-[110px] p-5 flex items-center justify-center">
                        <div className="flex flex-col justify-center items-center">
                            <div className="bg-[#9FCDFF] p-1 pl-2 pr-2 rounded-2xl font-inter-r text-center">Calories</div>
                            <div className={`text-center text-[#ffff] font-inter-r ${f1} `}>{v1}</div>
                        </div>
                        <div className={`flex justify-center items-center ${t1}`}>
                            <div onClick={() => {seth1("hidden"); seti1("");}} className={`${h1} bg-p w-[50px] h-[50px] bg-cover bg-center hover:scale-105 duration-500 ease-in-out cursor-pointer`}></div>
                            <div className={`${i1} bg-[#073575] w-[130px] h-[60px] flex justify-center items-center rounded-3xl translate-x-[40px]`}>
                                <form onSubmit={handleSubmit}>
                                    <input className={` w-[120px] h-[50px] bg-[#B0D1FF] flex items-center rounded-2xl outline-none p-2 caret-white text-[20px] text-black number-input`} type="number" min="0" max="5000" onChange={handleChange1}></input>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div className="w-[125px] h-[550px] flex justify-center rounded-full bg-[#D9D9D9]/30 overflow-hidden">
                        <div className={`w-[130px] h-[400px] bg-bb2 rounded-full`}></div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Page;
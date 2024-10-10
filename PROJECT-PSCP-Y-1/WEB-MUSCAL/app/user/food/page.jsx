import Link from "next/link";

const Page=()=>{
    return(
        <div className="w-screen h-screen flex flex-col p-[20px]">
            <div className="font-krona-r text-[#E44545] text-[60px]">Food <span className="text-[#ffff]">Log</span></div>
            <div className="flex items-center">
                <Link href="/user/food/addfood">
                    <div className="bg-bb1 flex items-center p-1 rounded-2xl pr-4 pl-4 hover:scale-105 duration-500 ease-in-out cursor-pointer gap-1">
                        <div className="text-[25px] text-[#ffff] font-inter-r text-center">Add food</div>
                        <div className="bg-cl hover:bg-p duration-500 ease-in-out bg-cover bg-center w-[50px] h-[50px]"></div>
                    </div>
                </Link>
            </div>
        </div>
    )
}
export default Page;
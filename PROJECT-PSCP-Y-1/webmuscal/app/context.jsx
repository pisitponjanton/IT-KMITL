"use client";
import { usePathname } from 'next/navigation';
import React, { createContext, useState,useEffect } from 'react';
const FoodContext = createContext();

export const FoodProvider = ({ children }) => {
  const parname = usePathname()

  const [totalCalories, setTotalCalories] = useState(0);
  const [totalprotein, setTotalprotein] = useState(0);
  const [totalcarbohydrate, setTotalcarbohydrate] = useState(0);
  const [totalfat, setTotalfat] = useState(0);

  const [username, setusername] = useState('');
  const [password, setpassword] = useState('');
  const [hh,sethh] = useState('translate-x-[-100vw]')
  const login1 = async () => {
    try {
      const response = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Login successful:', data);
        localStorage.setItem('position', username)
        localStorage.setItem('Authorization',data.user.access)
        window.location.href = '/user';
      } else {
        sethh("translate-x-[0vw]")
      }
    }catch (error) {
      console.log('Login error')
    }
  };

  const [confirm_password,setccpassword] = useState('')
  const register1 = async () => {
    try {
      const response1 = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/auth/register',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password,confirm_password}),
      });
      if (response1.ok) {
          const data = await response1.json();
          alert("Register successful")
          window.location.href = '/';
      } else {
        sethh("translate-x-[0vw]")
      }
    }catch (error) {
      console.log('Login error')
    }
  };

  const [foodList, setFoodList] = useState([]);
  const foodV = async () => {
    try {
      const foodve = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/foods/view_all_food', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
      });
      if (foodve.ok) {
        const data = await foodve.json();
        setFoodList(data.food_items);
      }else if(foodve.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      } else {
        console.log('Error fetching food items: Status', foodve.status);
      }
    } catch (error) {
      console.log('Error fetching food items:', error);
    }
  };
  
  const [food_name, setfood_name] = useState('');
  const [serving_size, setserving_size] = useState('');
  const [servings_per_container, setservings_per_container] = useState('');
  const [calories_per_serving, setcalories_per_serving] = useState('');
  const [carbohydrates_per_serving,setcarbohydrates_per_serving] = useState('')
  const [protein_per_serving,setprotein_per_serving] = useState('')
  const [fat_per_serving,setfat_per_serving] = useState('')
  const foodadd = async (e) => {
    e.preventDefault();
    try {
      const addf = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/foods/add_food',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
        body: JSON.stringify({ food_name, serving_size ,servings_per_container,calories_per_serving,carbohydrates_per_serving,protein_per_serving,fat_per_serving}),
      });
      if (addf.ok) {
        window.location.reload();
      }else if(addf.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      }else {
        const data = await addf.json();
        console.log(data)
        alert("Food name, serving size, servings per container, and calories per serving are required.")
      }
    }catch (error) {
      console.log('Food item added error.')
    }
  };

  const [dayd,setdayd] = useState("")
  
  const [vfood,setvfood] = useState('')
  const vfoodlog = async () => {
    try {
      const vlogfood = await fetch(`https://muscal-api-9078d108b990.herokuapp.com/muscal-api/log/view_log/`,{
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
      });
      if (vlogfood.ok) {
        const data = await vlogfood.json();
        setvfood(data)
        setdayd(cdata)
        setTotalCalories(data.total_calories)
        setTotalprotein(data.total_protein)
        setTotalcarbohydrate(data.total_carbohydrates)
        setTotalfat(data.total_fat)
      }else if(vlogfood.status === 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      }else if(vlogfood.status === 404 ){
        console.log("NOT FOUND")
      }
    }catch (error) {
      console.log("EE:",error)
      console.log(formattedDate)
    }
  };

  const logfood = async (food_id, quantity) => {
    try {
      const lonfood = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/log/log_food',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
        body: JSON.stringify({cdata, food_id, quantity}),
      });
      if (lonfood.ok) {
        window.location.href="/user/food"
        foodV();
      }else if(lonfood.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      } else {
        const data = await lonfood.json();
        console.log(data)
      }
    }catch (error) {
      console.log('Food item added error.')
    }
  };

  const [calorie_goal,setcalories] = useState('')
  const [protein_goal,setprotein] = useState('')
  const [carbohydrate_goal,setcarbohydrate] = useState('')
  const [fat_goal,setfat] = useState('')

  const [cdata,setcdata] = useState('')
  const [cdata1,setcdata1] = useState('')
  const [calorie_progress,setcalorie_progress] = useState('')
  const [protein_progress,setprotein_progress] = useState('')
  const [carbohydrate_progress,setcarbohydrate_progress] = useState('')
  const [fat_progress,setfat_progress] = useState('')
  const [day2,setday2] = useState('hidden')
  const [dd,setdd] = useState('')
  const [mm,setmm] = useState('')
  const [yy,setyy] = useState('')

  const [cc,setcc] = useState(0)
  const [cct,setcct] = useState("Submit")
  const cd = () => {
    if(!cc){
     setcc(1)
     setcct("Confirm")
    }else{
      setday2("hidden");
      setcct("Submit")
      setcc(0)
    }
    const dataToStore = `${yy}-${mm}-${dd}`;
    setcdata(dataToStore);
    db()
  };

  const db = async () => {
    try {
      const dbtop = await fetch(`https://muscal-api-9078d108b990.herokuapp.com/muscal-api/user/dashboard?log_date=${cdata}`,{
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
      });
      if (dbtop.ok) {
        const data = await dbtop.json();
        console.log(cdata)
        setcdata1(data.log_date)
        setcalories(Math.ceil(data.goal.calorie_goal))
        setprotein(Math.ceil(data.goal.protein_goal))
        setcarbohydrate(Math.ceil(data.goal.carbohydrate_goal))
        setfat(Math.ceil(data.goal.fat_goal))
        
        setcalorie_progress(Math.ceil(data.progress.calorie_progress))
        setprotein_progress(Math.ceil(data.progress.protein_progress))
        setcarbohydrate_progress(Math.ceil(data.progress.carbohydrate_progress))
        setfat_progress(Math.ceil(data.progress.fat_progress))
        
        setvfood(data)
        setdayd(cdata)
        setTotalCalories(data.total.total_calories)
        setTotalprotein(data.total.total_protein)
        setTotalcarbohydrate(data.total.total_carbohydrates)
        setTotalfat(data.total.total_fat)
        
      }else if(dbtop.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      }
    }catch (error) {
      console.log("EE:")
    }
  };
  

  const setgoal = async () => {
    try {
      const setg = await fetch('https://muscal-api-9078d108b990.herokuapp.com/muscal-api/user/set_goal',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
        body: JSON.stringify({calorie_goal,protein_goal,carbohydrate_goal,fat_goal}),
      });
      if (setg.ok) {
        const data = await setg.json();
        setcalories(data.goal.calorie_goal)
        setprotein(data.goal.protein_goal)
        setcarbohydrate(data.goal.carbohydrate_goal)
        setfat(data.goal.fat_goal)
        window.location.href = '/user';
      }else if(setg.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      }else if (setg.status === 400) {
        alert("Sum of protein, carbohydrate, and fat goals cannot exceed 100.")
      }else {
        console.log("top:",error)
      }
    }catch (error) {
      console.log('Setgoal error.')
    }
  };

  const delog = async (eid) => {
    try {
      const delogf = await fetch(`https://muscal-api-9078d108b990.herokuapp.com/muscal-api/log/delete_food_entry/${eid}`,{
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('Authorization')}`
        },
      });
      if (delogf.ok) {
        window.location.href = '/user/food/';
        console.log("DELETE ID:",eid)
        foodV();
      }else if(delogf.status == 401){
        localStorage.setItem('position','')
        localStorage.setItem('Authorization','')
      }
    }catch (error) {
      console.log('Setgoal error.')
    }
  };

  const [token, setToken] = useState(null)

  const tt = {"top":"1234","test":"12344"};
  const [name2,setname2] = useState(null)

  useEffect(() => {
    if(parname !== "/"){
      db();
      foodV();
      vfoodlog();
    }
    if(parname === "/user/food/" || parname === "user/food/addfood/"){
      foodV();
    }
  }, [parname]);
  useEffect(()=>{
    const nnn = localStorage.getItem("position")
    if(nnn){
      setname2(nnn)
    }
  },[name2])

  return (
    <FoodContext.Provider value={{
      calorie_goal,protein_goal,carbohydrate_goal,fat_goal
      ,setcalories,setprotein,setcarbohydrate,setfat,
      
      foodList,

      foodadd,
      food_name,setfood_name,
      serving_size, setserving_size,
      servings_per_container, setservings_per_container,
      calories_per_serving, setcalories_per_serving,
      carbohydrates_per_serving,setcarbohydrates_per_serving,
      protein_per_serving,setprotein_per_serving,
      fat_per_serving,setfat_per_serving,

      vfood,

      dayd,setdayd,
      setgoal,
      logfood,

      calorie_progress,
      protein_progress,
      carbohydrate_progress,
      fat_progress,
      
      setcdata,cdata1,db,

      setday2,
      setdd,
      setmm,
      setyy,
      day2,
      cd,
      cct,
      delog,

      totalCalories,setTotalCalories,totalprotein, setTotalprotein,totalcarbohydrate,setTotalcarbohydrate,totalfat, setTotalfat,
      token,setToken,
      name2,tt,password,setpassword,username,setusername
      ,login1,hh,sethh,
      setccpassword,register1}}>
      {children}
    </FoodContext.Provider>
  );
};

export default FoodContext;

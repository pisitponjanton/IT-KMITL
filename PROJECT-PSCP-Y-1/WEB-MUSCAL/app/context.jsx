"use client";
import React, { createContext, useState } from 'react';
const FoodContext = createContext();

export const FoodProvider = ({ children }) => {
  const [calories,setcalories] = useState(2000)
  const [protein,setprotein] = useState(70)
  const [carbohydrate,setcarbohydrate] = useState(200)
  const [fat,setfat] = useState(68)

  const [foodList, setFoodList] = useState([]);
  const [foodName, setFoodName] = useState('');
  const [addcalories, setaddcalories] = useState('');
  const [addprotein,setaddprotein] = useState('')
  const [addcarbohydrate,setaddcarbohydrate] = useState('')
  const [addfat,setaddfat] = useState('')

  const [totalCalories, setTotalCalories] = useState(0);
  const [totalprotein, setTotalprotein] = useState(0);
  const [totalcarbohydrate, setTotalcarbohydrate] = useState(0);
  const [totalfat, setTotalfat] = useState(0);
  return (
    <FoodContext.Provider value={{calories,protein,carbohydrate,fat,setcalories,setprotein,setcarbohydrate,setfat,
      addcalories,addprotein,addcarbohydrate,addfat,setaddcalories,setaddprotein,setaddcarbohydrate,setaddfat,
      foodList,setFoodList,foodName,setFoodName,
      totalCalories,setTotalCalories,totalprotein, setTotalprotein,totalcarbohydrate,setTotalcarbohydrate,totalfat, setTotalfat}}>
      {children}
    </FoodContext.Provider>
  );
};

export default FoodContext;

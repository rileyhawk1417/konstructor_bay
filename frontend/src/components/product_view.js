"use client"

import Image from 'next/image'
import { TbShoppingCartPlus } from "react-icons/tb";
import { useRef, useEffect } from 'react'
import { addItem } from '@/app/tools';
export function ProductView(props) {
  let valueRef = useRef()
  function alertBox(itemName) {
    let amount = valueRef.current.value
    addItem(itemName, amount)
    alert(`Added ${amount} ${itemName}(s)`)
  }
  return (
    <>

      <Image src="/assets/images/traffic_cone_4.jpg" className="max-w-sm rounded-lg shadow-2xl" width={500} height={500} />
      <div className="flex-col lg:flex-row">
        <div>
          <h1 className="text-5xl font-bold">{props.itemName}</h1>
          <p className="py-6">{props.itemDesc}</p>
          <div className="flex flex-row justify-between">
            <span className="flex flex-row justify-evenly items-center pl-10 pr-10">
              <p className="pr-8">Quantity: </p>
              <input ref={valueRef} type='number' className="w-16 h-12 rounded-md text-center" />
            </span>
            <button onClick={() => alertBox(props.itemName)} className="btn btn-primary">Add to cart <TbShoppingCartPlus size={24} /> </button>
          </div>
        </div>
      </div>
    </>
  )
}

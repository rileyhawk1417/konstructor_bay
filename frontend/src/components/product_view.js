"use client";

import Image from "next/image";
import { TbShoppingCartPlus } from "react-icons/tb";
import { useRef, useEffect } from "react";
import { addItem } from "@/app/tools";
export function ProductView(props) {
  return (
    <div className="grid grid-cols-2 items-start justify-center sm:grid-cols-1 gap-[50px]">
      <div className="w-max">
        <Image
          src="/assets/images/traffic_cone_4.jpg"
          className="max-w-sm rounded-lg shadow-2xl"
          width={500}
          height={500}
        />
        <div className="flex-col lg:flex-row">
          <div>
            <h1 className="text-5xl font-bold">{props.itemName}</h1>
            <p className="py-6">{props.itemDesc}</p>
            <div className="flex flex-row justify-between">
              <span className="flex flex-row justify-evenly items-center pl-10 pr-10">
                <p className="pr-8">Quantity: </p>
                <input
                  type="number"
                  className="w-16 h-12 rounded-md text-center"
                />
              </span>
              <button
                onClick={() => alertBox(props.itemName)}
                className="btn btn-primary"
              >
                Add to cart <TbShoppingCartPlus size={24} />{" "}
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="w-max flex flex-col items-start justify-center ">
        <header className="text-4xl underline underline-off-set-4 pb-8">
          Supplier Information
        </header>
        <div className="grid grid-cols-2 items-start gap-8">
          <span>Supplier name:</span>{" "}
          <span>{props.supplier_name ? props.supplier_name : "Unknown"}</span>
        </div>
        <div className="grid grid-cols-2 items-start justify-items-start gap-4">
          <span>Phone no.:</span>{" "}
          <span>{props.phone_no ? props.phone_no : "No phone number"}</span>
        </div>
        <div className="grid grid-cols-2 items-start justify-items-start gap-4">
          <span>Does delivery:</span>{" "}
          <span>{props.delivery ? props.delivery : "False"}</span>
        </div>
        <div className="grid grid-cols-2 items-start justify-items-start gap-4">
          <span>Email: </span>{" "}
          <span>{props.email ? props.email : "No Email"}</span>
        </div>
      </div>
    </div>
  );
}

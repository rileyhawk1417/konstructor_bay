"use client";

import Image from "next/image";
import { TbShoppingCartPlus } from "react-icons/tb";
import { useRef, useState, useEffect } from "react";

async function addToCart(user_id, itemId, qty) {
  let data = await fetch(
    `http://localhost:5000/api/cart/create_cart/${user_id}`,
  );
  let reply = await data.json();

  let addItem = await fetch("http://localhost:5000/api/cart/add_product", {
    method: "POST",
    mode: "cors",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      cart_id: reply.cart_id,
      product_id: itemId,
      qty: qty,
    }),
  });
  let addItemReply = await addItem.json();
  console.log(addItemReply);
}

export function ProductView(props) {
  let valueRef = useRef();
  const [uid, setUID] = useState(null);
  const [qty, setQty] = useState(0);
  useEffect(() => {
    let s = document.cookie.indexOf("user_id");
    let e = document.cookie.substring(s + 8, document.cookie.length);
    setUID(e);
  }, [uid]);
  return (
    <>
      <Image
        src="/assets/images/traffic_cone_4.jpg"
        className="max-w-sm rounded-lg shadow-2xl"
        width={500}
        height={500}
        alt="Picture of asset being sold"
      />
      <div className="flex-col lg:flex-row">
        <div>
          <h1 className="text-5xl font-bold">{props.itemName}</h1>
          <p className="py-6">{props.itemDesc}</p>
          <div className="flex flex-row justify-between">
            <span className="flex flex-row justify-evenly items-center pl-10 pr-10">
              <p className="pr-8">Quantity: </p>
              <input
                ref={valueRef}
                type="number"
                className="w-24 h-12 rounded-md text-center input "
                onChange={(e) => setQty(e.target.value)}
              />
            </span>
            <button
              onClick={async () => addToCart(uid, props.itemId, qty)}
              className="btn btn-primary"
            >
              Add to cart <TbShoppingCartPlus size={24} />{" "}
            </button>
          </div>
        </div>
      </div>
    </>
  );
}

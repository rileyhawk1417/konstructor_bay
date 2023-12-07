"use client";

import { Button } from "@nextui-org/react";

async function addProduct(name, desc, qty, price, id, business_name) {
  try {
    const data = await fetch(`http://localhost:5000/api/products`, {
      method: "POST",
      mode: "cors",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        product_name: name,
        description: desc,
        quantity: qty,
        price: price,
        supplier_id: id,
        business_name: business_name,
      }),
    });
    let reply = await data.json();
    return reply;
  } catch (e) {
    console.log(e);
  }
}

export default function AddInventory(props) {
  return (
    <div>
      <header className="text-2xl" id="addProduct">
        Add a product
      </header>
      <form
        className="flex flex-col items-start justify-start gap-4"
        action={async (formData) => {
          const name = formData.get("name");
          const desc = formData.get("desc");
          const price = formData.get("price");
          const qty = formData.get("qty");
          const d = addProduct(
            name,
            desc,
            qty,
            price,
            props.supplier_id,
            props.business_name != null ? "" : props.business_name,
          );
          console.log(d);
        }}
      >
        <div className="grid grid-cols-2 items-center">
          <span className="">Product Name</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs "
            name="name"
          />
        </div>

        <div className="grid grid-cols-2 items-center">
          <span className="">Description</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs "
            name="desc"
          />
        </div>

        <div className="grid grid-cols-2 items-center">
          <span className="">Quantity</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs "
            name="qty"
          />
        </div>

        <div className="grid grid-cols-2 items-center">
          <span className="">Price Per Unit</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs"
            name="price"
          />
        </div>

        <Button type="submit">Add Product</Button>
      </form>
    </div>
  );
}

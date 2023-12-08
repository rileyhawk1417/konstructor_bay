"use client";

import { BsTrash } from "react-icons/bs";
import { Button } from "@nextui-org/react";

const globalDay = new Date();
//TODO: Add alert to avoid accidental deletion
const deleteProduct = async (id) => {
  try {
    await fetch(`http://localhost:5000/api/products/${id}`, {
      method: "DELETE",
    }).catch((e) => console.log(e));
  } catch (e) {
    console.log(e);
  }
};
export default function InventoryTable(props) {
  return (
    <div id="current_inventory" className="flex flex-col">
      <header className="text-4xl">Inventory</header>
      <div className="grid grid-cols-6 sticky">
        <div>Date Received</div>
        <div>Item Name</div>
        <div>Price per item</div>
        <div>Quantity</div>
        <div>Total Price</div>
        <div>Actions</div>
      </div>

      <div className="overflow-y-scroll h-96">
        {props.data.map((item, keys) => (
          <div key={keys} className="grid grid-cols-6 gap-4 p-4">
            <div>{`${globalDay.getDate()}/${globalDay.getMonth()}/${globalDay.getFullYear()}`}</div>
            <div>{item.product_name}</div>
            <div>{item.price}</div>
            <div>{item.quantity}</div>
            <div>${item.quantity * item.price}</div>
            <div>
              <Button onClick={() => deleteProduct(item.id)} color="danger">
                <BsTrash />{" "}
              </Button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

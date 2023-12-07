"use client";
import { useState } from "react";
import { Button } from "@nextui-org/react";
const registerSupplier = async (id, supplierName, supplierEmail, phone_no) => {
  try {
    let data = await fetch(`http://localhost:5000/api/add_supplier`, {
      method: "POST",
      mode: "cors",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        supplier_name: supplierName,
        email: supplierEmail,
        user_id: id,
        phone_num: phone_no,
      }),
    });
    let reply = await data.json();
    if (reply.includes("registered")) {
      return reply;
    } else if (reply.includes("success")) {
      return reply;
    } else {
      return reply;
    }
  } catch (e) {
    console.log(e);
  }
};

export default function RegisterSupplier(props) {
  const [status, setStatus] = useState();
  return (
    <div>
      <form
        className="flex flex-col items-center justify-center gap-4"
        action={async (formData) => {
          const email = formData.get("email");
          const supplierName = formData.get("supplier_name");
          const supplierPhone = formData.get("supplier_phone");
          let d = registerSupplier(
            props.user_id,
            supplierName,
            email,
            supplierPhone,
          );
          setStatus(d);
        }}
      >
        <div className="grid grid-cols-2 gap-2 items-center">
          <span>username</span>
          <input
            type="text"
            value={props.username}
            className="input input-bordered w-full max-w-xs "
            name="username"
          />
        </div>

        <div className="grid grid-cols-2 gap-2 items-center">
          <span>email</span>
          <input
            type="text"
            value={props.email}
            className="input input-bordered w-full max-w-xs "
            name="email"
          />
        </div>

        <div className="grid grid-cols-2 gap-2 items-center">
          <span>Supplier Name</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs "
            name="supplier_name"
          />
        </div>
        <div className="grid grid-cols-2 gap-2 items-center">
          <span>Supplier Phone no.</span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs "
            name="supplier_phone"
          />
        </div>
        <Button type="submit">Register</Button>
      </form>
      {status != null ? (
        <div className="h-44 m-4 rounded-md bg-slate-700 grid grid-cols-1 items-center justify-items-center self-center">
          {status}
        </div>
      ) : null}
    </div>
  );
}

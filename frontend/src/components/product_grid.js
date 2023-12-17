"use client";

import Image from "next/image";
import Link from "next/link";

/*
 * NOTE: The product card takes the following
 *  itemID
 *  itemName
 *  itemDesc
 *  quantity
 *  supplierName
 *  itemPrice
 *
 *  NOTE:
 *  props makes it easier to get other values like:
 *  props.name
 *  Makes it easier instead of writing name, which is hard to use
 */

export function ProductCard(props) {
  return (
    <Link href={`/product/${props.itemID}`}>
      <div className="card w-96  bg-base-100 shadow-xl" key={props.keyID}>
        <figure>
          <Image
            src="/assets/images/traffic_cone_4.jpg"
            height={500}
            width={500}
            alt="Traffic cone image"
            loading="lazy"
          />
        </figure>
        <div className="card-body">
          <h2 className="card-title">Name: {props.itemName}</h2>
          <p>{props.itemDesc}</p>
          <p>Quantity: {props.quantity}</p>
          <p>Supplier {props.supplierName}</p>
          <div className="card-actions items-center justify-evenly">
            <p className="card-title text-2xl">${props.itemPrice}</p>
            <Link href="#">
              {props.isCart ? (
                <button
                  className="btn btn-error text-white"
                  onClick={async () => {
                    await fetch(
                      "http://localhost:5000/api/cart/remove_product",
                      {
                        method: "POST",
                        mode: "cors",
                        headers: {
                          Accept: "application/json",
                          "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                          cart_id: props.cartID,
                          product_id: props.itemID,
                        }),
                      },
                    );
                  }}
                >
                  Remove From Cart
                </button>
              ) : (
                <button className="btn btn-primary">Buy Now</button>
              )}
            </Link>
          </div>
        </div>
      </div>
    </Link>
  );
}

export default function ProductGrid(props) {
  return (
    <div className="grid grid-cols-4 gap-8 ">
      {props.data.map((item, idx) => (
        <ProductCard
          key={idx + 1}
          keyID={idx}
          itemID={item.id}
          itemName={item.product_name}
          itemDesc={item.description}
          quantity={item.quantity}
          supplierName={item.supplier_name}
          itemPrice={item.price}
          isCart={props.isCart}
          cartID={props.cardID}
        />
      ))}
    </div>
  );
}

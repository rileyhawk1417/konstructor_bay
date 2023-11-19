import { nanoid } from "nanoid";
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

function ProductCard(props) {
  return (
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
          <p className="card-title text-2xl">{props.itemPrice}</p>
          <Link href="#">
            <button className="btn btn-primary">Buy Now</button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function ProductGrid(props) {
  return (
    <div className="grid grid-cols-4 gap-8 ">
      {props.data.map((item, idx) => (
        <ProductCard
          keyID={idx}
          itemID={item.itemID}
          itemName={item.itemName}
          itemDesc={item.itemDesc}
          quantity={item.quantity}
          supplierName={item.supplier}
          itemPrice={item.price}
        />
      ))}
    </div>
  );
}

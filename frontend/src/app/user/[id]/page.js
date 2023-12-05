import {
  itemNames,
  generateIndex,
  generatePrice,
  priceFormatter,
} from "@/app/tools";
import Link from "next/link";
import { Button } from "@nextui-org/react";

function transactionHistory() {
  const day = new Date();
  return new Array(50).fill(null).map(() => ({
    date: `${day.getDate()}/${day.getMonth()}/${day.getFullYear()}`,
    itemName: itemNames[generateIndex(itemNames.length)],
    pricePerItem: priceFormatter.format(generatePrice()),
    quantity: generateIndex(200),
    total: priceFormatter.format(generateIndex(20) * generatePrice()),
  }));
}

export default function Home() {
  const data = transactionHistory();
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        <div
          id="profile_section"
          className="grid grid-cols-2 sm:grid-cols-1 gap-4 items-center justify-items-center pb-6"
        >
          <div className="rounded-full h-16 w-16 bg-slate-700 flex items-center justify-center">
            Profile
          </div>
          <div>Username</div>
          <div>
            <Link href={`/usr/${0}/addProduct`}>
              <Button>Add Product</Button>
            </Link>

            <Link href={`/usr/${0}/removeProduct`}>
              <Button>Remove Product</Button>
            </Link>
          </div>
        </div>
        <div
          id="stats"
          className="flex flex-row items-center justify-center gap-4 pb-4"
        >
          <div className=" bg-slate-700 rounded-full p-4 flex items-center justify-center">
            Products Sold: 80
          </div>
          <div className=" bg-slate-700 rounded-full p-4 flex items-center justify-center">
            Products Remaining: 350
          </div>
          <div className=" bg-slate-700 rounded-full p-4 flex items-center justify-center">
            Orders pending: None
          </div>
        </div>
      </div>
      <div id="transaction_history" className="flex flex-col">
        <div className="grid grid-cols-5 sticky">
          <div>Date</div>
          <div>Item Name</div>
          <div>Price per item</div>
          <div>Quantity</div>
          <div>Total Price</div>
        </div>
        <div className="overflow-y-scroll h-96">
          {data.map((item, keys) => (
            <div key={keys} className="grid grid-cols-5 gap-4">
              <div>{item.date}</div>
              <div>{item.itemName}</div>
              <div>{item.pricePerItem}</div>
              <div>{item.quantity}</div>
              <div>{item.total}</div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}

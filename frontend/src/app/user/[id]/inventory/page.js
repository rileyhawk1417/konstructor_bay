import {
  itemNames,
  generateIndex,
  generatePrice,
  priceFormatter,
} from "@/app/tools";
import Link from "next/link";
import { Button } from "@nextui-org/react";
import { global } from "styled-jsx/css";
import InventoryTable from "@/components/inventory_table";
import AddInventory from "@/components/add_product_form";
import TransactionHistory from "@/components/transaction_history";
export const dynamic = "force-dynamic";
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

export default async function Home(props) {
  const data = transactionHistory();

  let apiData = await fetch("http://localhost:5000/api/products").then((k) =>
    k.json(),
  );

  let fetchSupplierID = await fetch(
    `http://localhost:5000/api/auth/fetch_supplier_id/${props.params.id}`,
  ).then((k) => k.json());

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        <div
          id="profile_section"
          className="grid grid-cols-2 sm:grid-cols-1 gap-4 items-center justify-items-center pb-6"
        >
          <div className="rounded-full h-16 w-16 bg-slate-700 flex items-center justify-center">
            User
          </div>
          <div>Username</div>
          <div>
            <Link href="#addProduct">
              <Button>Add Product</Button>
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
      <InventoryTable data={apiData} />
      <AddInventory
        supplier_id={fetchSupplierID.supplier_id}
        business_name={fetchSupplierID.business_name}
      />
      <TransactionHistory data={data} />
    </main>
  );
}

import ProductGrid from "@/components/product_grid";
import { nanoid } from "nanoid";
export const dynamic = "force-dynamic";

const supplierNames = [
  "Braxton H/W",
  "Princeton",
  "Ableton H/W",
  "Maximus H/W",
  "OBJ Industries",
];

const itemNames = [
  "Cement",
  "Hammer",
  "Drill",
  "Quarry",
  "Wrench",
  "Scissors Jack",
];

const itemDescs = [
  "Important tool",
  "Very useful item",
  "Useful tool for most cases",
];

function generateIndex(num) {
  return Math.floor(Math.random() * (num - 1) + 1);
}

function generatePrice() {
  let curr = Math.random() * (100 - 10 + 1);
  let price = curr.toString().substring(0, 5);
  return price;
}

const priceFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

async function getProducts() {
  return new Array(100).fill(null).map(() => ({
    itemID: nanoid(),
    itemName: itemNames[generateIndex(itemNames.length)],
    itemDesc: itemDescs[generateIndex(itemDescs.length)],
    quantity: generateIndex(200),
    supplier: supplierNames[generateIndex(supplierNames.length)],
    price: priceFormatter.format(generatePrice()),
    image: "",
  }));
}

export default async function Home() {
  let product_data = await getProducts();
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        <ProductGrid data={product_data} />
      </div>
    </main>
  );
}

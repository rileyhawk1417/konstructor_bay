import ProductGrid from "@/components/product_grid";
export const dynamic = "force-dynamic";
import { getProducts } from "./tools";

export default async function Home() {
  //let product_data = await getProducts();
  let apiData = await fetch("http://localhost:5000/api/products").then((k) =>
    k.json(),
  );
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        <ProductGrid data={apiData} />
      </div>
    </main>
  );
}

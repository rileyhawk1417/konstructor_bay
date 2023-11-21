import ProductGrid from "@/components/product_grid";
export const dynamic = "force-dynamic";
import { getProducts } from "./tools";

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

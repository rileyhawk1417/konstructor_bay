import { getProducts } from "@/app/tools";
import { ProductView } from "@/components/product_view";

export default async function Page(props) {
  let data = await fetch(
    `http://localhost:5000/api/products/${props.params.id}`,
  ).then((k) => k.json());
  let res = data;

  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      <ProductView itemName={res.product_name} itemDesc={res.description} />
    </div>
  );
}

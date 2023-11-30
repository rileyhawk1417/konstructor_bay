import { getProducts } from "@/app/tools";
import { ProductView } from "@/components/product_view";

export default async function Page(props) {
  //let data = await getProducts()
  let data = await fetch("http://localhost:5000/api/products").then((k) =>
    k.json()
  );
  let res;
  data.map((item) => {
    if (item.id === props.params.id) {
      console.log("Found a match!");
      res = item;
    }
  });

  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      <ProductView
        itemName={res.product_name}
        itemDesc={res.description}
      />
    </div>
  );
}

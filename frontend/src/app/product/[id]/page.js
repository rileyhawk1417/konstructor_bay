import { getProducts } from "@/app/tools";
import { ProductView } from "@/components/product_view";

export default async function Page(props) {
  let data = await fetch(
    `http://localhost:5000/api/products/${props.params.id}`,
  ).then((k) => k.json());
  let res = data;

  let supplier_data = await fetch(
    `http://localhost:5000/api/auth/fetch_supplier_info/${res.supplier_id}`,
  ).then((d) => d.json());
  console.log(supplier_data);

  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      <ProductView
        itemName={res.product_name}
        itemDesc={res.description}
        supplier_name={supplier_data.business_name}
        phone_no={supplier_data.phone_num}
        delivery={supplier_data.delivery}
        email={supplier_data.email}
      />
    </div>
  );
}

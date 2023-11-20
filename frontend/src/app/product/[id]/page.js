
import { getProducts } from '@/app/tools';
import { ProductView } from '@/components/product_view';


export default async function Page(props) {

  let data = await getProducts()
  let res;
  data.map((item) => {
    if (item.itemID === props.params.id) {
      res = item;
    }
  })

  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      <ProductView
        itemName={res.itemName}
        itemDesc={res.itemDesc}
      />
    </div>
  )
}

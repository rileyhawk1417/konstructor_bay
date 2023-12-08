import { getShoppingCart } from "../tools"


export default async function Page() {
  let x = await getShoppingCart()
  console.log(x)
  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      Hello World
    </div>
  )
}

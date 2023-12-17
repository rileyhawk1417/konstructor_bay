import ProductGrid from "@/components/product_grid";

export const dynamic = "force-dynamic";

async function fetchCart(id) {
  let find_cart = await fetch(`http://localhost:5000/api/cart/${id}`);
  let find_cart_result = await find_cart.json();
  if (find_cart_result.includes("does not exist")) {
    return "No items in cart!";
  } else {
    let cart = await fetch(
      `http://localhost:5000/api/cart/${id}/fetch/${find_cart_result}`,
    );
    let cart_reply = await cart.json();
    return cart_reply;
  }
}

async function fetchCartId(id) {
  let find_cart = await fetch(`http://localhost:5000/api/cart/${id}`);
  let find_cart_result = await find_cart.json();
  return find_cart_result;
}

export default async function Page(props) {
  let data = await fetchCart(props.params.id);
  let cartId = await fetchCartId(props.params.id);
  return (
    <div className="flex min-h-screen flex-col items-center justify-evenly p-24">
      <header className="text-4xl">Items In Cart</header>
      <br />
      {data && <ProductGrid data={data} isCart={true} cartID={cartId} />}
    </div>
  );
}

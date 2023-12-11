import ProductGrid from "@/components/product_grid";
export const dynamic = "force-dynamic";

async function fetchData(query) {
  try {
    let data = await fetch(`http://localhost:5000/api/search/${query}`).then(
      (d) => d.json(),
    );
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

export default async function Page(props) {
  let reply = await fetchData(props.params.query);
  console.log(reply.error);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        {reply.error == null ? (
          <ProductGrid data={reply} />
        ) : (
          <div>{reply.error}</div>
        )}
      </div>
    </main>
  );
}

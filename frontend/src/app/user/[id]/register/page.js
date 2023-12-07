import RegisterSupplier from "@/components/register_supplier";

async function fetchUserData(id) {
  let data = await fetch(`http://localhost:5000/api/auth/fetch_user/${id}`, {
    method: "POST",
  }).catch((e) => console.log(e));
  return data.json();
}

export default async function Page(props) {
  let reply = await fetchUserData(props.params.id);
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <header className="text-2xl p-4">Register as supplier!</header>
      <RegisterSupplier
        username={reply.username}
        email={reply.email}
        fname={reply.fname}
        lname={reply.lname}
        user_id={reply.user_id}
      />
    </main>
  );
}

import { Button } from "@nextui-org/react";
import LoginBox from "@/components/login_box";
export default function Page() {
  //let product_data = await getProducts();
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div>
        <LoginBox />
      </div>
    </main>
  );
}

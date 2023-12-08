"use client";

export default function TransactionHistory(props) {
  return (
    <div id="transaction_history" className="flex flex-col">
      <header className="text-4xl">Transaction History</header>
      <div className="grid grid-cols-5 sticky">
        <div>Date</div>
        <div>Item Name</div>
        <div>Price per item</div>
        <div>Quantity</div>
        <div>Total Price</div>
      </div>
      <div className="overflow-y-scroll h-96">
        {props.data.map((item, keys) => (
          <div key={keys} className="grid grid-cols-5 gap-4">
            <div>{item.date}</div>
            <div>{item.itemName}</div>
            <div>{item.pricePerItem}</div>
            <div>{item.quantity}</div>
            <div>{item.total}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

import { Button } from "@nextui-org/react";

export default function AddInventory() {
  return (
    <div>
      <form className="flex flex-col items-start justify-start">
        <label className="form-control w-full max-w-xs">
          <div className="label">
            <span className="label-text">Name of the product</span>
          </div>
        </label>
        <div className="join join-horizontal flex justify-center items-center">
          <span className="join-item flex items-center justify-center p-4">
            Product Name
          </span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs join-item"
          />
        </div>

        <label className="form-control w-full max-w-xs">
          <div className="label">
            <span className="label-text">Description of the product</span>
          </div>
        </label>
        <div className="join join-horizontal flex justify-center items-center">
          <span className="join-item flex items-center justify-center p-4">
            Description
          </span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs join-item"
          />
        </div>

        <label className="form-control w-full max-w-xs">
          <div className="label">
            <span className="label-text">The number of items</span>
          </div>
        </label>
        <div className="join join-horizontal flex justify-center items-center">
          <span className="join-item flex items-center justify-center p-4">
            Quantity
          </span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs join-item"
          />
        </div>

        <label className="form-control w-full max-w-xs">
          <div className="label">
            <span className="label-text">The individual price of the item</span>
          </div>
        </label>
        <div className="join join-horizontal flex justify-center items-center">
          <span className="join-item flex items-center justify-center p-4">
            Price Per Unit
          </span>
          <input
            type="text"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs join-item"
          />
        </div>
      </form>
      <Button type="submit">Submit</Button>
    </div>
  );
}

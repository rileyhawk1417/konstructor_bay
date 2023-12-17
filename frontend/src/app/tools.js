export const supplierNames = [
  "Braxton H/W",
  "Princeton",
  "Ableton H/W",
  "Maximus H/W",
  "OBJ Industries",
];

export const itemNames = [
  "Cement",
  "Hammer",
  "Drill",
  "Quarry",
  "Wrench",
  "Scissors Jack",
];

const randomUUIDList = [
  "4f2b47e0-5f9c-44dc-8df5-dabfb1db7104",
  "1e7d6bc6-5d69-41a9-9588-9677d74c1395",
  "add2713c-a12f-4924-9a21-19fdfc7ba7d1",
  "2e609695-06d3-45da-abd6-bee06ecab741",
  "c695d45e-43e1-4280-89ed-d9d8b97ddd18",
  "91294cf5-d43c-482b-8285-e1adc8602b02",
];

const itemDescs = [
  "Important tool",
  "Very useful item",
  "Useful tool for most cases",
];

export function generateIndex(num) {
  return Math.floor(Math.random() * (num - 1) + 1);
}

export function generatePrice() {
  let curr = Math.random() * (100 - 10 + 1);
  let price = curr.toString().substring(0, 5);
  return price;
}

export const priceFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

export async function getProducts() {
  return new Array(itemNames.length).fill(null).map(() => ({
    itemID: randomUUIDList[generateIndex(randomUUIDList.length)],
    itemName: itemNames[generateIndex(itemNames.length)],
    itemDesc: itemDescs[generateIndex(itemDescs.length)],
    quantity: generateIndex(200),
    supplier: supplierNames[generateIndex(supplierNames.length)],
    price: priceFormatter.format(generatePrice()),
    image: "",
  }));
}
let cartItems = [];

export function addItem(itemName, quantity) {
  cartItems.push({ name: itemName, quantity: quantity });
}

export function deleteItem(itemName) {
  cartItems.map((item, idx) => {
    if (item.name === itemName) {
      cartItems.splice(idx, 1);
    }
  });
}

export async function getShoppingCart() {
  console.log(cartItems);
  return cartItems;
}

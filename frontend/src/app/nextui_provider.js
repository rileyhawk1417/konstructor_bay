"use client";
import { NextUIProvider } from "@nextui-org/react";

export default function NXProvider({ children }) {
  return <NextUIProvider>{children}</NextUIProvider>;
}

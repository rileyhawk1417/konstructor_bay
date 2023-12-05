"use client";
import { useState, useEffect } from "react";
import { Button } from "@nextui-org/react";
function ErrMsgBox() {
  return (
    <div role="alert" className="alert alert-error">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="stroke-current shrink-0 h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
      <span>Invalid Credentials!</span>
    </div>
  );
}
export default function LoginBox() {
  const [errMsg, setErrMsg] = useState(false);
  async function onSubmit(user, pass) {
    const response = await fetch("http://localhost:5000/api/auth/login", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      mode: "cors",
      body: JSON.stringify({
        username: user,
        password: pass,
      }),
    });

    // Handle response if necessary
    const data = await response.json();
    const reply = data.toString();
    //TODO: Get back user ID for url
    if (reply.includes("success")) {
      console.log("Login Successful");
      ("use server");
      document.cookie = "login_status=true; SameSite=None; Secure";
      setTimeout(() => {
        window.location.replace("/user/1/profile");
      }, 3000);
    } else {
      console.log("Invalid credentials");
      setErrMsg(true);
    }
    // ...
  }
  return (
    <div className="flex flex-col items-center gap-4 bg-slate-700 p-24 ">
      <header className="text-4xl">Login</header>
      <form
        action={async (formData) => {
          const u = formData.get("userName");
          const p = formData.get("passWord");
          onSubmit(u, p);
        }}
        className="grid auto-rows-max gap-4"
      >
        <div className="flex flex-row justify-between ">
          <span>Username</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="text" name="userName" className="input" />
        </div>
        <div>
          <span>Password</span>
          <span className="pl-4 pr-4" />
          <input id="pass" type="text" name="passWord" className="input" />
        </div>
        <Button type="submit" className="bg-slate-800">
          Login
        </Button>
      </form>
      {errMsg && <ErrMsgBox />}
    </div>
  );
}

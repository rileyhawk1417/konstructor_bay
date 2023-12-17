"use client";

import Link from "next/link";
import React, { useEffect, useState } from "react";
import { BsCart4 } from "react-icons/bs";
import { Button } from "@nextui-org/react";
/*
 * To avoid writing large code in one function.
 * It helps to split them like below
 * The Profile button is separate and can easily be included
 * in the main function
 */
//TODO: Cookie Function
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function ProfileDropDown() {
  const [cookie, setCookie] = useState(false);
  const [uid, setUid] = useState(null);
  useEffect(() => {
    const strippedCookie = document.cookie.substring(
      13,
      document.cookie.length,
    );
    //TODO: Solve cookie issue
    let s = document.cookie.indexOf("user_id");
    let e = document.cookie.substring(s + 8, document.cookie.length);
    setUid(e);

    if (strippedCookie) {
      setCookie(true);
    } else {
      setCookie(false);
    }
  }, []);
  return (
    <div className="dropdown dropdown-end flex-[0.5] flex justify-end pr-4">
      <label tabIndex={0} className="btn btn-ghost btn-circle ">
        <div className="w-10 rounded-full flex justify-center items-center">
          User
        </div>
      </label>
      <ul
        tabIndex={0}
        className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52"
      >
        <li>
          {cookie ? (
            <Link
              href={`/user/${uid}/profile`}
              replace
              className="justify-between"
            >
              Profile
            </Link>
          ) : null}
        </li>
        <li>
          <Link
            href={`/cart/${uid}/`}
            className="flex flex-row items-center justify-between"
          >
            <span>Cart</span>
            <BsCart4 size={24} />
          </Link>
        </li>
        <li>
          <Link href="#">Settings</Link>
        </li>
        <li>
          {cookie ? (
            <Link
              href="#"
              onClick={() =>
                (document.cookie = "login_status=false; SameSite=None; Secure")
              }
            >
              Logout
            </Link>
          ) : (
            <Link href="/user" replace>
              Login
            </Link>
          )}
        </li>
      </ul>
    </div>
  );
}

export default function NavBar() {
  const [query, setQuery] = useState("");
  return (
    <div className="navbar sticky top-0 z-10 bg-slate-700">
      <Link href="/" className="flex-[0.5]">
        Konstructor Bay
      </Link>
      <form
        className="form-control flex-[0.5] flex flex-row "
        action={async (formData) => {
          //NOTE: Empty Space
        }}
      >
        <input
          type="text"
          className="input input-bordered w-full md:w-auto"
          name="product_search"
          onChange={(e) => {
            setQuery(e.target.value);
          }}
        />
        <span className="ml-2 mr-2" />
        <Link href={`/search/${query}`}>
          <Button type="button">Search</Button>
        </Link>
      </form>
      <ProfileDropDown />
    </div>
  );
}

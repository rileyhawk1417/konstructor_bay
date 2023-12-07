"use client";

import Link from "next/link";
import React, { useEffect, useState } from "react";
import { BsCart4 } from "react-icons/bs";
/*
 * To avoid writing large code in one function.
 * It helps to split them like below
 * The Profile button is separate and can easily be included
 * in the main function
 */

function ProfileDropDown() {
  const [cookie, setCookie] = useState(false);
  useEffect(() => {
    const strippedCookie = document.cookie.substring(
      13,
      document.cookie.length,
    );
    if (strippedCookie) {
      setCookie(true);
    } else {
      setCookie(false);
    }
  }, []);
  return (
    <div className="dropdown dropdown-end flex-[1] flex justify-end pr-4">
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
            <Link href="/usr/1/profile" replace className="justify-between">
              Profile
            </Link>
          ) : null}
        </li>
        <li>
          <Link
            href="/cart"
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
  return (
    <div className="navbar sticky top-0 z-10 bg-slate-700">
      <div className="flex-[0.5]">Konstructor Bay</div>
      <div className="flex-1 gap-2">
        <div className="form-control flex-1">
          <input type="text" className="input input-bordered w-24 md:w-auto" />
        </div>
        <ProfileDropDown />
      </div>
    </div>
  );
}

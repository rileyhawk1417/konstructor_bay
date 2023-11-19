import Link from "next/link";
/*
 * To avoid writing large code in one function.
 * It helps to split them like below
 * The Profile button is separate and can easily be included
 * in the main function
 */
function ProfileDropDown() {
  return (
    <div className="dropdown dropdown-end flex-[1] flex  justify-end pr-4">
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
          {/* Link from nextJS is like the <a></a>*/}
          <Link href="#" className="justify-between">
            Profile <span className="badge">New</span>
          </Link>
        </li>
        <li>
          <Link href="#">Settings</Link>
        </li>
        <li>
          <Link href="#">Logout</Link>
        </li>
      </ul>
    </div>
  );
}

export default function NavBar() {
  return (
    <div className="navbar">
      <div className="flex-[0.5]">Konstructor Bay</div>
      <div className=" gap-2">
        <div className="form-control flex-1">
          <input type="text" className="input input-bordered w-24 md:w-auto" />
        </div>
        <ProfileDropDown />
      </div>
    </div>
  );
}

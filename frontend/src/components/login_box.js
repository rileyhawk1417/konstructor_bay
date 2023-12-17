"use client";
import { useState, useEffect } from "react";
import { Button } from "@nextui-org/react";
function WelcomeBox(props) {
  return (
    <div role="alert" className="alert alert-success">
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
          d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
      <div className="flex flex-row items-center justify-evenly">
        <span>Welcome {props.username}</span>

        <svg
          class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          ></circle>
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
      </div>
    </div>
  );
}
function ErrMsgBox(props) {
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
      <span>{props.msg}</span>
    </div>
  );
}

function SignUpBox() {
  const [errMsg, setErrMsg] = useState(false);
  const [welcomeMsg, setWelcomeMsg] = useState(false);
  const [username, setUsername] = useState("");
  const [pass, setPass] = useState("");
  const [pass_2, setPass_2] = useState("");
  const [match, setMatch] = useState(false);
  const [err, setErr] = useState("");

  // Handle response if necessary
  let user_id = "";
  let loginStatus = "";
  async function onSubmit(user, pass, fname, lname, email) {
    try {
      const response = await fetch("http://localhost:5000/api/auth/register", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        mode: "cors",
        body: JSON.stringify({
          username: user,
          first_name: fname,
          second_name: lname,
          email: email,
          password: pass,
        }),
      });
      let reply = await response.json();
      loginStatus = reply.message;
      user_id = reply.user_id;
    } catch (e) {
      console.log(e);
    }

    if (loginStatus != null && loginStatus.includes("success")) {
      console.log("Login Successful");
      setUsername(user);
      setWelcomeMsg(true);
      setErr(loginStatus);
      document.cookie = "login_status=true; SameSite=None; Secure";
      document.cookie = `user_id=${user_id}; SameSite=None; Secure`;
      setTimeout(() => {
        window.location.replace(`/user/${user_id}/profile`);
      }, 3000);
    } else {
      console.log("Invalid credentials");
      setErr(err);
      setErrMsg(true);
      setTimeout(() => {
        setErrMsg(false);
      }, 10000);
    }
  }

  useEffect(() => {
    if (pass.length != 0 && pass_2.length != 0 && pass === pass_2) {
      setMatch(true);
    } else {
      setMatch(false);
    }
  }, [pass, pass_2]);
  return (
    <div className="flex flex-col items-center gap-4  p-12 ">
      <header className="text-4xl">SignUp</header>
      <form
        action={async (formData) => {
          const user = formData.get("userName");
          const pass = formData.get("passWord");
          const fname = formData.get("fname");
          const lname = formData.get("lname");
          const email = formData.get("email");
          onSubmit(user, pass, fname, lname, email);
        }}
        className="grid  auto-rows-max gap-4"
      >
        <div className="flex flex-row items-center justify-between ">
          <span>Username</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="text" name="userName" className="input" />
        </div>
        <div className="flex flex-row items-center justify-between ">
          <span>First Name</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="text" name="fname" className="input" />
        </div>
        <div className="flex flex-row items-center justify-between ">
          <span>Last Name</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="text" name="lname" className="input" />
        </div>
        <div className="flex flex-row items-center justify-between ">
          <span>Email</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="email" name="email" className="input" />
        </div>
        <div className="flex flex-row items-center justify-between">
          <span>Password</span>
          <span className="pl-4 pr-4" />
          <input
            id="pass"
            type="password"
            name="passWordFirst"
            className="input"
            onChange={(e) => setPass(e.target.value)}
          />
        </div>
        <div className="flex flex-row items-center justify-between">
          <span>Confirm Password</span>
          <span className="pl-4 pr-4" />
          <input
            id="pass"
            type="password"
            name="passWordConfirm"
            className="input"
            onChange={(e) => setPass_2(e.target.value)}
          />
        </div>
        <Button type="submit" className="bg-white text-black">
          Login
        </Button>
      </form>
      {match && <div>Passwords Match!</div>}
      {!match && <div>Passwords Dont Match!</div>}
      {errMsg && <ErrMsgBox msg={err} />}
      {welcomeMsg && <WelcomeBox username={username} />}
    </div>
  );
}

function SignInBox() {
  const [errMsg, setErrMsg] = useState(false);
  const [welcomeMsg, setWelcomeMsg] = useState(false);
  const [username, setUsername] = useState("");
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
    let user_id = "";
    let loginStatus = "";
    const data = await response
      .json()
      .then((obj) => {
        loginStatus = obj.message;
        user_id = obj.user_id;
      })
      .catch((e) => console.error(e));
    console.log(loginStatus);
    console.log(user_id);
    if (loginStatus != null && loginStatus.includes("success")) {
      console.log("Login Successful");
      setUsername(user);
      setWelcomeMsg(true);
      document.cookie = "login_status=true; SameSite=None; Secure";
      document.cookie = `user_id=${user_id}; SameSite=None; Secure`;
      setTimeout(() => {
        window.location.replace(`/user/${user_id}/profile`);
      }, 3000);
    } else {
      console.log("Invalid credentials");
      setErrMsg(true);
    }
    // ...
  }
  return (
    <div className="flex flex-col items-center gap-4  p-12 ">
      <header className="text-4xl">Login</header>
      <form
        action={async (formData) => {
          const u = formData.get("userName");
          const p = formData.get("passWord");
          onSubmit(u, p);
        }}
        className="grid auto-rows-max gap-4"
      >
        <div className="flex flex-row items-center justify-between ">
          <span>Username</span>
          <span className="pl-4 pr-4" />
          <input id="user" type="text" name="userName" className="input" />
        </div>
        <div className="flex flex-row items-center justify-between">
          <span>Password</span>
          <span className="pl-4 pr-4" />
          <input id="pass" type="password" name="passWord" className="input" />
        </div>
        <Button type="submit" className="bg-white text-black">
          Login
        </Button>
      </form>
      {errMsg && <ErrMsgBox msg="Invalid Credentials!" />}
      {welcomeMsg && <WelcomeBox username={username} />}
    </div>
  );
}

export default function LoginBox() {
  const [login, setLogin] = useState(false);
  const [newUser, setNewUser] = useState("");
  useEffect(() => {
    if (login) {
      setNewUser("Create a new account");
    } else {
      setNewUser("Login to your account");
    }
  }, [login]);
  return (
    <div className="flex bg-slate-700 flex-col items-center justify-center p-4 rounded-md">
      <a
        className="text-center m-[12px] cursor-pointer link text-xl  text-white"
        onClick={() => setLogin(!login)}
      >
        {newUser}
      </a>
      {login && <SignInBox />}
      {!login && <SignUpBox />}
    </div>
  );
}

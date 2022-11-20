import { apple, bill, google } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button";
import './login.css';


import React, { useState } from "react";

function Login({ setUserData, setUser, user }) {

  const fetchData = () => {
    return fetch("http://localhost:8080/getData", {
      method: 'POST',
      // mode: 'no-cors',
      headers: {
        'AcceptAccess-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "login": user.login,
        "password": user.password
      }),
      redirect: "follow"
    });
  }

  const submitHandler = e => {
    e.preventDefault();

    fetchData().then(res => res.json()).then(res => {
      setUserData(res["data"])
      console.log(res["data"])
    })

  }
  return (
    <section id="login" className={layout.sectionReverse}>

      <div className={layout.sectionInfo}>
        <h2 className={styles.heading2}>
          Log in <br className="sm:block hidden" /> To Your Secure Key Manager
        </h2>

          <div className="grid">
            <form action="https://httpbin.org/post" method="POST" className="form login">
              <div className="form__field">
                <span className="hidden">Username</span>
                <input id="login__username" type="text" name="username" className="form__input" 
                  placeholder="Username"  onChange={e => setUser({ ...user, login: e.target.value })} value={user.email} required />
              </div>

              <div className="form__field">
                <span className="hidden">Password</span>
                <input id="login__password" type="password" name="password" className="form__input" 
                onChange={e => setUser({ ...user, password: e.target.value })} value={user.password} placeholder="Password" required />
              </div>

              <div className="form__field">
                <input type="submit" value="Sign In" onClick={submitHandler} />
              </div>
            </form>
          </div>

      </div>

    </section>
  );
}



export default Login;

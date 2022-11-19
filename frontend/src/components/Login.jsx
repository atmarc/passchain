import { apple, bill, google } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button";

import React, { useState } from "react";

function Login () {
  const [details, setDetails] = useState({email: "", password: ""});

  const fetchData = async () => {
    const response = await fetch("https://reqbin.com/echo/post/json", {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: `{
    "Login": ${details.email},
    "Password": ${details.password},,
    }`,
    });
    return response
  }

  const submitHandler = e => {
    e.preventDefault();

    // console.log(details);

    data = fetchData()
    data.json().then(data => {
      console.log(data);
      
    });
  }
  return (
    <section id="login" className={layout.sectionReverse}>

      <div className={layout.sectionInfo}>
        <h2 className={styles.heading2}>
          Log in <br className="sm:block hidden" /> to your secure key manager
        </h2>
        <form onSubmit={submitHandler}>
          <div className="form-inner">
            <div className="form-group">
              <label style={{color: "white"}} htmlFor="email" >
                Email: 
              </label>
              <input type="email" name="email" id="email" onChange={e => setDetails({ ...details, email: e.target.value})} value={details.email}/>
            </div>
            <div className="form-group">
              <label style={{ color: "white" }} htmlFor="password">
                Password:
              </label>
              <input type="password" name="password" id="password" onChange={e => setDetails({ ...details, password: e.target.value })} value={details.password} />
            </div>
          </div>
        </form>

        <button style={{ color: "white" }} onClick={submitHandler}>Sign In</button>
      </div>

    </section>
  );
}



export default Login;

import styles from "./style";
import { Login, Business, CardDeal, Clients, CTA, Footer, Navbar, Stats, Testimonials, Hero} from "./components";
import React, {useState} from "react";

function App() {
  const adminUser = {
    email: "admin@chainpass.com",
    password: "password"
  }

  const [user, setUser] = useState({email: "", password: ""});

  // const LoginFunction = details =>{
  //   console.log(details);
  // }
  
  return (
    <div className="bg-primary w-full overflow-hidden">
      <div className={`${styles.paddingX} ${styles.flexCenter}`}>
        <div className={`${styles.boxWidth}`}>
          <Navbar />
        </div>
      </div>

      <div className={`bg-primary ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <Hero />
        </div>
      </div>
      
      <div className={`bg-primary ${styles.paddingX} ${styles.flexCenter}`}>
        <div className={`${styles.boxWidth}`}>
          <Stats />
          <Business />
          <Login />
          <CardDeal />
          <Testimonials />
          <Clients />
          <CTA />
          <Footer />
        </div>
      </div>

      {/* <div className = "App">
        {(user.email != "") ? (
          <div className="welcome">
            <h2>
              Welcome, <span>{user.name}</span>
            </h2>
          </div>
        ): 
        (
          <Login />
        )
        }
      </div> */}
    </div>
  );
}

export default App;

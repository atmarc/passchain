import styles from "./style";
import { Login, Business, CardDeal, Clients, CTA, Footer, Navbar, Stats, Testimonials, Hero} from "./components";
import React, {useState} from "react";

function App() {
  const adminUser = {
    email: "admin@chainpass.com",
    password: "password"
  }

  const [user, setUser] = useState({login: "", password: ""});
  const [userData, setUserData] = useState([]);
  
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
          <Login setUserData={setUserData} setUser={setUser} user={user} />
          <CardDeal setUserData={setUserData} userData={userData} user={user} />
          <Footer />
        </div>
      </div>

    </div>
  );
}

export default App;

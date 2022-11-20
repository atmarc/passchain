import { card } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button";
import BasicTable from "./Table";


const user_pw = [{"login": 'hi', "password": 'pw'}, {"login": 'wo', "password": 'pw2'}]
const listItems = user_pw.map((item) =>
  <li>
    {item["login"]} 
    {item["password"]} 
  </li>
)

const CardDeal = ({ userData }) => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Find a better card deal <br className="sm:block hidden" /> in few easy
        steps.
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        Arcu tortor, purus in mattis at sed integer faucibus. Aliquet quis
        aliquet eget mauris tortor.ç Aliquet ultrices ac, ametau.
      </p>
      {/* <Button styles={`mt-10`} /> */}

      <BasicTable userData={userData} />

    </div>

    {/* <div className={layout.sectionImg}>
      <img src={card} alt="billing" className="w-[100%] h-[100%]" />
    </div> */}
  </section>
);

export default CardDeal;

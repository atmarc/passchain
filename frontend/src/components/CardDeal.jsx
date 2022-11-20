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

      <BasicTable userData={userData} />

    </div>
  </section>
);

export default CardDeal;

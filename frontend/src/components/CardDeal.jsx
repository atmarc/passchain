import { card } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button";
import BasicTable from "./Table";

const CardDeal = ({ userData, user }) => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>

      <BasicTable userData={userData} user={user} />

    </div>
  </section>
);

export default CardDeal;

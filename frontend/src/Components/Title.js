import { Link } from "react-router-dom";

const Title = () =>{
    return (
        <div  className="header">
            <div class="logo"><Link to="/">📚</Link></div>
            <nav>
                <Link to="/list">書籍列表</Link>
                <Link to="/addbook">新增書籍</Link>
                <Link to="/statistics">資料統計</Link>
            </nav>
        </div>
    );
  };
  
  export default Title;

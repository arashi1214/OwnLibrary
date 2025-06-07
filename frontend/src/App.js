import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';



import { BrowserRouter, Route, Routes} from "react-router-dom"

import './App.css';
import Bookpage from "./BookList/Bookpage";
import Title from './Components/Title';
import AddBook from "./BookCRUD/AddBook";


function App() {
  return (
    <BrowserRouter>
      <Title />
      <Routes>
        <Route path="/" element={<Bookpage />} />
        <Route path="/list"/>
        <Route path="/addBook" element={<AddBook />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;


import './App.css';
import Title from './Components/Title';
import BookForm from './BookList/BookForm';
import Result from './Components/Result';

function App() {
  return (
    <div className="App">
      <Title></Title>
      <BookForm></BookForm>
      <Result></Result>
    </div>
  );
}

export default App;

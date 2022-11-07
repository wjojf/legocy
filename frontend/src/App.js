import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';


import './App.css';
import Header from './components/Header'
import SetsListPage from './pages/SetsListPage'
import SetPage from './pages/SetPage'

function App() {
  return (
    <Router>
      
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" exact element={<SetsListPage />}></Route>
          <Route path='/set/:setId' element={<SetPage/>}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;

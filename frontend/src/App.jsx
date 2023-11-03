import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Layout from './components/layout';
import HomePage from './pages/HomePages';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';


function App() {
  const [] = useState();

  return (
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Layout />}>
            <Route index element={<HomePage />}/>
            <Route path='login' element={<LoginPage />}/>
            <Route path='register' element={<RegisterPage />}/>
          </Route>
        </Routes>
      </BrowserRouter>
  );
}

export default App;
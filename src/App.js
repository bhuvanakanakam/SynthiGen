import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import * as Components from './components';
import { Footer, Header, WhatSynthiGen } from './containers';
import { Navbar, Datagenerator, Login, SignUp } from './components';
import './App.css';

const App = () => {
    return (
        <div className="App">
            <div className="gradient__bg">
                <Router>
                    <Navbar />
                    <Header />
                    <Routes>
                        <Route path="/login" element={<Login />} />
                        <Route path="/signUp" element={<SignUp />} />
                    </Routes>
                </Router>
            </div>
            <Datagenerator />
            <WhatSynthiGen />
            <Footer />
        </div>
    );
};


export default App;

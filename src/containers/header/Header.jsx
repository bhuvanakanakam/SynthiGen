import React from 'react';
import './header.css';

const Header = () => {
    return (
        <div className="synthiGen__header section__padding gradient__bg" id="home">
            <div className="synthiGen__header-content">
                <h1 className='gradient__text'>Synthetic Dataset Generator</h1>
                <p> Create dynamic, diverse, and data-rich landscapes with our user-friendly schema-driven tool. <br></br>
                    Craft Parquet datasets tailored to your needs, supporting varied data types and relationships, for unique cases.</p>
                <div className="synthiGen__header-content__input">
                    <input type="email" placeholder="Enter your email address" />
                    <button type="button" className="big-button w-inline-block">Get Started</button>
                </div>
            </div>
        </div>
    );
}

export default Header;

import React from 'react'
import './whatSynthiGen.css';
import { Feature } from '../../components';

const WhatSynthiGen = () => {
    return (
        <div className="synthiGen__whatSynthiGen section__margin" id="whatSynthiGen">
            <div className="synthiGen__whatSynthiGen-feature">
                <Feature title="What is SynthiGen" text="At SynthiGen, we understand the importance of data in today's information-driven world. Whether you're a software developer, a data analyst, or a business owner, having access to diverse and realistic data is crucial for various applications, from testing your software to making informed decisions." />
            </div>
            <div className="synthiGen__whatSynthiGen-heading">
                <h1 className="gradient__text">Create Custom Synthetic Data Effortlessly </h1>
            </div>
            <div className="synthiGen__whatSynthiGen-container">
                <Feature title="Schema Definition" text="Allow users to define their data schema in a text area." />
                <Feature title="User Authentication" text="Implement secure user authentication with JWT." />
                <Feature title="Download Options" text="Provide download options for generated data (Parquet, CSV)." />
            </div>
        </div>
    )
}

export default WhatSynthiGen
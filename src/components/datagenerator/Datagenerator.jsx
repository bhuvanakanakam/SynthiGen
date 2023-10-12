import React, { useState } from 'react';
import './datagenerator.css';

const DataGenerator = () => {
    const [selectedTemplate, setSelectedTemplate] = useState('select');
    const [attributes, setAttributes] = useState([]);
    const [numColumns, setNumColumns] = useState(1);
    const [numRows, setNumRows] = useState(1);

    const handleGenerateDataset = () => {
        // Handle the generation of the dataset based on your attributes and number of rows.
        // You can use this function to create and format your dataset.
        // This example simply logs the dataset to the console.
        console.log(attributes);
    };

    const handleDownloadDataset = () => {
        // Handle the download functionality here.
        // You can create and initiate a download of the dataset.
        // This example is just a placeholder for demonstration.
        console.log('Downloading dataset...');
    };
    const handleTemplateChange = (e) => {
        setSelectedTemplate(e.target.value);
        if (e.target.value === 'select') {
            setAttributes([]);
        } else if (e.target.value === 'hospital') {
            setAttributes([
                { name: 'Patient ID', fieldType: 'id', constraint: 'enter length of the id' },
                { name: 'Patient Name', fieldType: 'name', constraint: '' },
                { name: 'Gender', fieldType: 'gender', constraint: '' },
                { name: 'Age', fieldType: 'age', constraint: 'enter min age, enter max age' },
                { name: 'Admission Date', fieldType: 'admission_date', constraint: 'enter the start date in the format[-1y]' },
                { name: 'Doctor Name', fieldType: 'name', constraint: '' },
                { name: 'Department', fieldType: 'department', constraint: '' },
                { name: 'Diagnosis', fieldType: 'diagnosis', constraint: '' },
                { name: 'Treatment', fieldType: 'treatment', constraint: '' },
                { name: 'Previous Records', fieldType: 'boolean', constraint: '' },
            ]);
        } else if (e.target.value === 'insurance') {
            setAttributes([
                { name: 'Policy ID', fieldType: 'id', constraint: 'enter length of the id' },
                { name: 'Policy Holder', fieldType: 'name', constraint: '' },
                { name: 'Insurance Company', fieldType: 'company', constraint: '' },
                { name: 'Coverage Type', fieldType: 'coverage_type', constraint: '' },
                { name: 'Premium Amount', fieldType: 'random_float', constraint: 'enter min range, enter max range' },
                { name: 'Policy Start Date', fieldType: 'start_date', constraint: 'enter start date[in the format \' -5y\']' },
                { name: 'Policy End Date', fieldType: 'end_date', constraint: 'enter end date[in the format \' +2y\']' },
                { name: 'Claim Amount', fieldType: 'claim_amount', constraint: '' },
                { name: 'Claim Date', fieldType: 'claim_date', constraint: '' },
            ]);
        }
    };

    const handleAttributeChange = (index, field, value) => {
        const newAttributes = [...attributes];
        newAttributes[index][field] = value;
        setAttributes(newAttributes);
    };

    const handleNumColumnsChange = (e) => {
        const newNumColumns = parseInt(e.target.value, 10);
        setNumColumns(newNumColumns);
        setAttributes(new Array(newNumColumns).fill({ name: '', fieldType: 'number', constraint: '' }));
    };

    const handleNumRowsChange = (e) => {
        const value = parseInt(e.target.value, 10);
        setNumRows(value);
    };

    return (
        <div className="synthiGen__datagenerator section__padding gradient__bg" id="dataGeneration">
            <h1 className="gradient__text">Data Generator</h1>
            <label htmlFor="template">Select Dataset:</label>
            <select
                name="template"
                id="template"
                value={selectedTemplate}
                onChange={handleTemplateChange}
            >
                <option value="select">Select Your Own</option>
                <option value="hospital">Hospital</option>
                <option value="insurance">Insurance</option>
            </select>
            <div className="synthiGen__header-content__input">
                <label htmlFor="num_columns">Number of Columns:</label>
                <input
                    type="number"
                    name="num_columns"
                    id="num_columns"
                    min="1"
                    required
                    value={numColumns}
                    onChange={handleNumColumnsChange}
                />
                <label htmlFor="num_rows">Number of Rows:</label>
                <input
                    type="number"
                    name="num_rows"
                    id="num_rows"
                    min="1"
                    required
                    value={numRows}
                    onChange={handleNumRowsChange}
                />
                <table>
                    <thead>
                        <tr>
                            <th>Field Name</th>
                            <th>Field Type</th>
                            <th>Constraints</th>
                        </tr>
                    </thead>
                    <tbody>
                        {attributes.map((attribute, index) => (
                            <tr key={index}>
                                <td>
                                    <input
                                        type="text"
                                        value={attribute.name}
                                        onChange={(e) => handleAttributeChange(index, 'name', e.target.value)}
                                    />
                                </td>
                                <td>
                                    <select
                                        value={attribute.fieldType}
                                        onChange={(e) => handleAttributeChange(index, 'fieldType', e.target.value)}
                                    >
                                        <option value="number">Number</option>
                                        <option value="string">String</option>
                                        <option value="dropdown">Dropdown</option>
                                    </select>
                                </td>
                                <td>
                                    <input
                                        type="text"
                                        value={attribute.constraint}
                                        onChange={(e) => handleAttributeChange(index, 'constraint', e.target.value)}
                                        placeholder="Constraint"
                                    />
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <button onClick={handleGenerateDataset}>Generate Dataset</button>
                <button onClick={handleDownloadDataset}>Download Dataset</button>
            </div>
        </div>
    );
};

export default DataGenerator;

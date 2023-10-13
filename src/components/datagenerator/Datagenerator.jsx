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
        } else if (e.target.value === 'choose_your_own') {
            setAttributes([
                // Add your desired options here
                { name: 'Number', fieldType: 'number', constraint: 'Numeric constraint enter the input format (eg: 12345)' },
                { name: 'First Name', fieldType: 'first_name', constraint: '' },
                { name: 'Female First Name', fieldType: 'first_name_female', constraint: '' },
                { name: 'Male First Name', fieldType: 'first_name_male', constraint: '' },
                { name: 'Female Name', fieldType: 'name_female', constraint: '' },
                { name: 'Male Name', fieldType: 'name_male', constraint: '' },
                { name: 'Last Name', fieldType: 'last_name', constraint: '' },
                { name: 'Email', fieldType: 'email', constraint: '' },
                { name: 'Phone Number', fieldType: 'phone_number', constraint: '' },
                { name: 'Birth Date', fieldType: 'birth_date', constraint: '' },
                { name: 'Date', fieldType: 'date', constraint: '' },
                { name: 'Month', fieldType: 'month', constraint: '' },
                { name: 'Month Name', fieldType: 'month_name', constraint: '' },
                { name: 'Year', fieldType: 'year', constraint: '' },
                { name: 'Time', fieldType: 'time', constraint: '' },
                { name: 'Address', fieldType: 'address', constraint: '' },
                { name: 'City', fieldType: 'city', constraint: '' },
                { name: 'State', fieldType: 'state', constraint: '' },
                { name: 'Country', fieldType: 'country', constraint: '' },
                { name: 'Zip Code', fieldType: 'zip_code', constraint: '' },
                { name: 'Department', fieldType: 'department', constraint: '' },
                { name: 'Job', fieldType: 'job', constraint: '' },
                { name: 'Salary', fieldType: 'salary', constraint: '' },
                { name: 'Color', fieldType: 'color', constraint: '' },
                { name: 'Boolean', fieldType: 'boolean', constraint: '' },
                { name: 'Company', fieldType: 'company', constraint: '' },
                { name: 'Company Suffix', fieldType: 'company_suffix', constraint: '' },
                { name: 'Weekday Name', fieldType: 'weekday_name', constraint: '' },
                { name: 'Language', fieldType: 'language', constraint: '' },
                { name: 'Credit Card Number', fieldType: 'credit_card_number', constraint: '' },
                { name: 'Credit Card Provider', fieldType: 'credit_card_provider', constraint: '' },
                { name: 'Credit Card Expire Date', fieldType: 'credit_card_expiredate', constraint: 'Alpha Numeric constraint enter the input format (eg: abc23d)' },
                { name: 'Alpha Numeric', fieldType: 'alpha_numeric', constraint: 'Numeric_Relation constraint enter the attribute which you want to relate' },
                { name: 'Numeric', fieldType: 'numeric', constraint: 'Numeric constraint enter the input format (eg: 12345)' },
                { name: 'Numeric_Relation', fieldType: 'numeric_relation', constraint: 'enter the attribute which you want to relate' },
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
                                        <option value="date">Date</option>
                                        <option value="month">Month</option>
                                        <option value="month_name">Month Name</option>
                                        <option value="year">Year</option>
                                        <option value="time">Time</option>
                                        <option value="address">Address</option>
                                        <option value="city">City</option>
                                        <option value="state">State</option>
                                        <option value="country">Country</option>
                                        <option value="zip_code">Zip Code</option>
                                        <option value="department">Department</option>
                                        <option value="job">Job</option>
                                        <option value="salary">Salary</option>
                                        <option value="color">Color</option>
                                        <option value="boolean">Boolean</option>
                                        <option value="company">Company</option>
                                        <option value="company_suffix">Company Suffix</option>
                                        <option value="weekday_name">Weekday Name</option>
                                        <option value="language">Language</option>
                                        <option value="credit_card_number">Credit Card Number</option>
                                        <option value="credit_card_provider">Credit Card Provider</option>
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

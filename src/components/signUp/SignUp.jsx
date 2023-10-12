import React, { useState } from 'react';

const Signup = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleSignup = async (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert('Passwords do not match');
            return;
        }
        // Make an API request to the backend to handle user registration
        // Receive and store the token upon successful registration
    };

    return (
        <div>
            <h1>Sign Up</h1>
            <form onSubmit={handleSignup}>
                <input
                    type="email"
                    name="email"
                    placeholder="Email Address"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <br />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br />
                <input
                    type="password"
                    name="confirmPassword"
                    placeholder="Confirm Password"
                    required
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />
                <br />
                <input type="submit" value="Sign Up" />
            </form>
        </div>
    );
};

export default Signup;
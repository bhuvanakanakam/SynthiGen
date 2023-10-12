import './navbar.css';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';
import { Link } from 'react-router-dom';

const Navbar = () => {
    const scrollToSection = (id) => {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <div className="synthiGen__navbar">
            <div className="synthiGen__navbar-links">
                <div className="synthiGen__navbar-links_container">
                    <p onClick={() => scrollToSection('home')}>Home</p>
                    <p onClick={() => scrollToSection('whatSynthiGen')}>What is synthiGen?</p>
                    <p onClick={() => scrollToSection('dataGeneration')}>Data Generation</p>
                </div>
            </div>
            <div className="synthiGen__navbar-sign">
                <Link to="/login">
                    <button>Log in</button>
                </Link>
                <Link to="/signUp">
                    <button>Sign Up</button>
                </Link>
            </div>
        </div>
    );
};

export default Navbar;

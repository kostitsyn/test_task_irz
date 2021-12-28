import {NavLink} from "react-router-dom";
import c from './Navbar.module.css';


const Navbar = (props) => {
    return (
        <nav className={c.navbar}>
            <NavLink to='/'>Form</NavLink>
            <NavLink to='/table'>Table</NavLink>
        </nav>
    )
}

export default Navbar;
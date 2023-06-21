import React from "react";
import { Link } from "react-router-dom";
import logoContigoUrl from "../../img/Logo_Contigo1.png";
import "../../styles/navbar.css";

export const Navbar = () => {
  return (
    <div className="navbar navbar-light">
      <div className="container">
        <Link to="/">
          <span className="navbar logo">
            <img src={logoContigoUrl} />
          </span>
        </Link>

        <ul className="nav justify-content-end">
          <li className="nav-item">
            <Link to="/donar">
              <button className="btn">Donaciones</button>
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/informacion">
              <button className="btn" href="#">
                Sobre Nosotros
              </button>
            </Link>
          </li>
          <li className="nav-item ">
            <Link to="/contacto">
              <button className="btn" href="#">
                Contactanos
              </button>
            </Link>
          </li>

          <li>
            <Link to="/login">
              <button className="btn login" href="#">
                <i className="fa-solid fa-user"></i>
              </button>
            </Link>
          </li>

          <li>
            <Link to="/demo">
              <button className="btn lenguaje">
                <i className="fa-solid fa-earth-europe"></i>
              </button>
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

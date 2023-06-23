import React, { Component } from "react";
import logoCorazonUrl from "../../img/logo_contigo_corazon.png";
import "../../styles/footer.css";
import { Link } from "react-router-dom";

export const Footer = () => {
  return (
    <div className="container-fluid footer">
      <div className="row">
        <div className="col-2 logo-corazon">
          <img src={logoCorazonUrl} />
        </div>

        <div className="col-3">
          <ul>
            <li>Direccion</li>
            <li>Email</li>
            <li>Telefonos</li>
          </ul>
        </div>
        <div className="col-3 asociaciones">
          <ul>
            <Link to="/ong">
              <li>ASOCIACIONES y ONG</li>
            </Link>
            <Link to="/informacion">
              <li>SOBRE NOSOTROS</li>
            </Link>
            <Link to="/privacidad">
              <li>POLITICA DE PRIVACIDAD</li>
            </Link>
          </ul>
        </div>
        <div className="col icons align-self-center">
          <Link to="https://www.instagram.com/">
            <i class="fa-brands fa-instagram"></i>
          </Link>
          <Link to="https://www.facebook.com/">
            <i class="fa-brands fa-facebook"></i>
          </Link>
          <Link to="https://twitter.com/">
            <i class="fa-brands fa-twitter"></i>
          </Link>
          <Link to="https://www.youtube.com/">
            <i class="fa-brands fa-youtube"></i>
          </Link>
          <Link to="https://www.tiktok.com/en/">
            <i class="fa-brands fa-tiktok"></i>
          </Link>
        </div>
      </div>
    </div>
  );
};

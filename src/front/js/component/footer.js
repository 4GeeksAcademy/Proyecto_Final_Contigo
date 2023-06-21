import React, { Component } from "react";
import logoCorazonUrl from "../../img/logo_contigo_corazon.png";
import "../../styles/footer.css";

export const Footer = () => {
  return (
    <div className="container-fluid footer">
      <img src={logoCorazonUrl} />
    </div>
  );
};

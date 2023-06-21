import React, { useState } from "react";
import { Link } from "react-router-dom";

export const Ong_register = () => {
    const  [data, setData] = useState({})
    const [ success, setSuccess] = useState(false);

	const handleChange = (event) => {
		setData({...data, [event.target.id]: event.target.value})
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		console.log(data)

		const config = {
			method: 'POST',
			body: JSON.stringify(data),
			headers: { 
				'Content-Type': 'application/json'
			}
		}

		fetch(URL, config)
		.then(res => {
            if (!res.ok) {
                throw new Error('Error en la solicitud');
            }
            return res.json();
        })
        .then(response => {
            console.log('Exito:', response);
            setSuccess(true);
        })
		.catch(error => console.error('Eror:', error))
	}

    return (

        <>

            { success ? (
                <div> 
                    <p>¡Registro de la ONG realizado con éxito!</p>
					<p>Traer el códgio de la ONG desde el response para mostrarlo y explicar como funciona</p>
                </div>
            ) : (

			<form onSubmit={handleSubmit}>
				<div className="col-8 m-auto">
				<h3 className="display-6 text-primary"> Nuevo usuario de ONG </h3>
					<div className="mb-3">
						<label htmlFor="name" className="form-label">Nombre de la ONG</label>
						<input type="text" className="form-control" id="name" name="name" placeholder="Name" onChange={handleChange} />
					</div>
                    <div className="mb-3">
						<label htmlFor="cif" className="form-label">CIF</label>
						<input type="text" className="form-control" id="cif" name="cif" placeholder="CIF" onChange={handleChange} />
					</div>
					<div className="mb-3">
						<label htmlFor="Email" className="form-label">Email</label>
						<input type="email" className="form-control" id="email" name="email" placeholder="Email" onChange={handleChange}/>
					</div>
					<div className="mb-3">
						<label htmlFor="WebSite" className="form-label">Página Web</label>
						<input type="url" className="form-control" id="website" name="website" placeholder="Página Web" onChange={handleChange}/>
					</div>
                    
					
					<button type="submit" className="btn btn-primary mt-3" role="button">
						Registrar ONG
					</button>
				</div>
			</form>
            )};

			<div className="col-8 m-auto mt-2">
			<Link to="/"><button type="button" className="btn btn-light">
					Volver a inicio
				</button></Link>
				</div>
    		</>
	);
}
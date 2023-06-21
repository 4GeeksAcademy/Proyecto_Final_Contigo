import React, { useState } from "react";
import { Link } from "react-router-dom";

export const User_register = () => {
    const  [ data, setData ] = useState({})
    const [ success, setSuccess ] = useState(false);

	const handleChange = (event) => {
		setData({...data, [event.target.name]: event.target.value})
	}

	const handleSubmit = async (event) => {
		event.preventDefault();
		console.log(data);

        const codigoOng  = data.codigoOng;

        const validarCodigoOng = async (codigoOng) => {
            const url = `URL/validarCodigoOng?codigoOng=${codigoOng}`;
           
            try {
                const response = await fetch(url);
                return response.json();
            } catch (error) {
                console.error('Error:', error);
                throw error;
            }
            };
        

        try {
            const validacionResponse = await validarCodigoOng(codigoOng);

            if (validacionResponse.ok) {

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

                .catch(error => console.error('Eror:', error));

            } else {
                alert('El código de ONG no existe. Verifícalo e intenta nuevamente.');
                 }

            } catch (error) {
                console.error('Error:', error);
            }
            
        }
	

    return (

        <>

            { success ? (
                <div> 
                    <p>¡Registro realizado con éxito!</p>
                </div>
            ) : (

			<form onSubmit={handleSubmit}>
				<div className="col-8 m-auto">
				<h3 className="display-6 text-primary"> Nuevo usuario de ONG </h3>
					<div className="mb-3">
						<label htmlFor="name" className="form-label">Nombre</label>
						<input type="text" className="form-control" id="name" name="name" placeholder="Name" onChange={handleChange} />
					</div>
                    <div className="mb-3">
						<label htmlFor="surname" className="form-label">Apellidos</label>
						<input type="text" className="form-control" id="surname" name="surname" placeholder="Surname" onChange={handleChange} />
					</div>
					<div className="mb-3">
						<label htmlFor="Email" className="form-label">Email</label>
						<input type="email" className="form-control" id="email" name="email" placeholder="Email" onChange={handleChange}/>
					</div>
                    <div className="mb-3">
						<label htmlFor="Password" className="form-label">Password</label>
						<input type="password" className="form-control" id="password" name="password" placeholder="Password" onChange={handleChange}/>
					</div>
					<div className="mb-3">
						<label htmlFor="codigoOng" className="form-label">Código ONG</label>
						<input type="number" className="form-control" id="codigoOng" name="codigoOng" placeholder="Código de registro de ONG" onChange={handleChange}/>
					</div>
					<button type="submit" className="btn btn-primary mt-3" role="button">
						Crear Usuario
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
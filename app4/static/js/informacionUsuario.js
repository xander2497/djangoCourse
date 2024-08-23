function devolverPub(idPub)
{
    fetch(`/devolverPub?idPub=${idPub}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        tituloPub = document.getElementById('tituloPub')
        autorPub = document.getElementById('autorPub')
        descripcionPub = document.getElementById('descripcionPub')
        idPublicacion = document.getElementById('idPublicacion')
        comentariosTotales = document.getElementById('comentariosTotales')

        tituloPub.value = ''
        autorPub.value = ''
        descripcionPub.value = ''
        idPublicacion.innerHTML = ''
        comentariosTotales.innerHTML = ''
        
        tituloPub.value = data.titulo
        autorPub.value = `${data.nombreAutor} ${data.apellidoAutor}`
        descripcionPub.value = data.descripcion
        idPublicacion.innerHTML = String(idPub)

        for(let j = 0; j < data.datosComentarios.length; j++)
        {
            seccionComentario = `
            <div class="row mb-3">
                <div class="col-3">
                    ${data.datosComentarios[j][0]}
                </div>
                <div class="col-9">
                    ${data.datosComentarios[j][1]}
                </div>
            </div>
            `
            comentariosTotales.innerHTML = comentariosTotales.innerHTML + seccionComentario
        }
    })
}

function enviarComentario()
{
    url = '/publicarComentario'
    datos = {
        'comentario':document.getElementById('comentarioUsuario').value,
        'idPublicacion':document.getElementById('idPublicacion').innerHTML
    }
    fetch(url,
    {
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById('comentarioUsuario').value = ''
        devolverPub(document.getElementById('idPublicacion').innerHTML)
    })
}




function getCookie(name)
{
    let cookieValue = null;
    if (document.cookie && document.cookie !== "")
    {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++)
        {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "="))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
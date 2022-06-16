$("#btn-cargar").click(function (event) {
    event.preventDefault();
  
    var url = "https://random-data-api.com/api/cannabis/random_cannabis?size=1";
  
  //   fetch(url)
  //     .then((response) => {
  //       return response.json();
  //     })
  //     .then((data) => {
  //       console.log(data);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });
  
      fetch(url)
          .then(response => response.json())
          .then(data => 
              {
                  var $id_cannabis = $('<h1>').text(data[0].id);
                  var $uso_medico = $('<p>').text(data[0].medical_use);
                  var $tipo = $('<p>').text(data[0].type);
                  //console.log($contenido)
                  var $beneficio = $('<p>').text(data[0].health_benefit);
                  
  
                  //var $foto_cerveza = $("<p><img src='"+data[0].image_url+"'>");
  
                  // para limpiar el contedor antes de desplegar
                  $("#info").empty();
                  $('#info')
                      .append($id_cannabis)
                      .append($uso_medico)
                      .append($tipo)
                      .append($beneficio)
  
              })
          .catch(error => console.error(error));
  
  });
  
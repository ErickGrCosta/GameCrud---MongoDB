document.addEventListener('DOMContentLoaded', function() {

  $('form input[type="file"]').change(event => {
      let arquivos = event.target.files;
      if (arquivos.length === 0) {
        console.log('sem imagem pra mostrar')
      } else {
          if(arquivos[0].type == 'image/jpeg') {
            $('img').remove();
            let imagem = $('<img class="img-fluid">');
            imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
            $('figure').prepend(imagem);
          } else {
            alert('Formato não suportado')
          }
      }
    });

  const urlParams = new URLSearchParams(window.location.search); // Implementar nos apps da HCosta.
  const allfields = urlParams.get('fields')
  const titlefield = urlParams.get('title')
  const categoryfield = urlParams.get('category')
  const consolefield = urlParams.get('console')
  
  let phrases = {
    'empty': 'Você esqueceu de preencher todos os campos!',
    'titleempty': 'Você esqueceu de preencher o título!',
    'categoryempty': 'Você esqueceu de criar uma categoria!',
    'consoleempty': 'Você esqueceu de preencher o console!',
  }

  // const fields = document.querySelectorAll('input') // - Opção.
  const fields = [allfields, titlefield, categoryfield,consolefield]
  let alertmessage = ''

  // Minha opção original:
  for (let i = 0; i < fields.length; i++) {
    if (fields[i] != null) {
      alertmessage = fields[i]
    }
  }
  // Peters options:
  // fields.forEach(e=>{
  //   if(e){
  //     alertmessage = e
  //   }
  // })

  // alertmessage = fields.find(e => e != null)
  function sweetAlert(message) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: message
    })
  } 

  if (alertmessage){
    sweetAlert(phrases[alertmessage])
  }
   

  })

  function sweetDelete(e) {
    const delete_url = e.getAttribute('delete_url')

    Swal.fire({
    title: 'Tem certeza?',
    text: "Você não terá como recuperar!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sim, deletar!'
    }).then((result) => {
    if (result.isConfirmed) {
        window.location.href = delete_url;
    }
    })
}


 // function loadDoc() {
    //   const xhttp = new XMLHttpRequest();
    //   console.log('Antes');
    //   xhttp.onload = function() {
    //     console.log('RESPOSTA');
    //   }
    //   xhttp.open("GET", "/", false);
    //   xhttp.send();
    //   console.log('Depois');
    // }
    
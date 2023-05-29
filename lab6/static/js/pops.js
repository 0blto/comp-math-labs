function oops(msg) {
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: msg,
        showClass: {
          popup: 'animate__animated animate__fadeIn'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOut'
        }
      })
}

function success(msg) {
    Swal.fire({
        icon: 'success',
        title: 'Success',
        text: msg,
        showClass: {
          popup: 'animate__animated animate__fadeIn'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOut'
        }
    })
}

function share() {
  Swal.fire({
    title: 'Drain shawty',
    text: 'Lab №5, computational math',
    imageUrl: '../static/resources/achi-kochi.gif',
    padding: '3em',
    color: '#716add',
    timer: 10000,
    timerProgressBar: true
    })
}
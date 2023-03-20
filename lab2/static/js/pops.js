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
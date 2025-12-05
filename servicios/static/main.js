
document.addEventListener('DOMContentLoaded', function(){

    // RESERVAR SERVICIO 
    const reservarBtns = document.querySelectorAll('.reservar-btn');
    const reservaModalEl = document.getElementById('reservaModal');
    const servicioSeleccionadoEl = document.getElementById('servicioSeleccionado');
    const servicioInput = document.getElementById('servicioInput');

    let reservaModal = null;
    if (reservaModalEl){
        reservaModal = new bootstrap.Modal(reservaModalEl);
    }

    // Click en "Reservar"
    reservarBtns.forEach(btn => {
        btn.addEventListener('click', function(){
            const nombreServicio = this.dataset.nombre;

            // Mostrar en el modal
            servicioSeleccionadoEl.textContent = "Servicio seleccionado: " + nombreServicio;

            // Enviar al backend mediante input hidden
            servicioInput.value = nombreServicio;

            // Mostrar modal
            reservaModal.show();
        });
    });

    // No viaje al pasado
    const fechaInput = document.querySelector('input[name="fecha"]');
    if (fechaInput){
        const hoy = new Date().toISOString().split("T")[0];
        fechaInput.min = hoy;
    }

});
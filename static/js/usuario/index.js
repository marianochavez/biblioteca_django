function listadoUsuarios(){
    $.ajax({
        url: "/usuario/listar_usuario/",
        type:"get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_usuarios')){
                $('#tabla_usuarios').DataTable().destroy();
            }
            $('#tabla_usuarios tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1 ) + '</td>';
                fila += '<td>' + response[i]["fields"]['username'] + '</td>';
                fila += '<td>' + response[i]["fields"]['name'] + '</td>';
                fila += '<td>' + response[i]["fields"]['last_name'] + '</td>';
                fila += '<td class="text-lowercase">' + response[i]["fields"]['email'] + '</td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal(edicion,\'/usuario/actualizar_usuario/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm"';
                fila += 'onclick = "abrir_modal(eliminacion,\'/usuario/eliminar_usuario/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';
                $('#tabla_usuarios tbody').append(fila);
            }
            $('#tabla_usuarios').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                        "first": "Primero",
                        "last": "Ultimo",
                        "next": "Siguiente",
                        "previous": "Anterior"
                    },
                },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
function registrar() {
    activarBoton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoUsuarios();
            cerrar_modal(creacion);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}
function editar(){
    activarBoton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoUsuarios();
            cerrar_modal(edicion);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        }
    });
}
function eliminar(pk) {
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/usuario/eliminar_usuario/'+pk+'/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoUsuarios();
            cerrar_modal(eliminacion);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}
$(document).ready(function (){
    listadoUsuarios();
});
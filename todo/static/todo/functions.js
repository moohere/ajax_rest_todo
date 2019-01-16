// Once the add button is clicked, calls AJAX POST request, which sends the title and due_date over to the add/ url
$(document).ready(function() {
    $(document).on("click", ".add", function(){
        $('#title').focus();

        $.ajax({
            type:'POST',
            url: 'add/',
            data: {
                    title : $('#title').val(),
                    due_date: $('#dueDate').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
        });
    });
});

// Once the edit button is clicked, calls AJAX POST request, which sends the same as add as well as id over to /edit
$(document).ready(function() {
    $(document).on("click", ".edit", function(){
        var id_num = $(this).data('id');
        $('#title').focus();
        if($('#title').val() !== ""){
            $.ajax({
                type:'POST',
                url: 'edit/',
                data: {
                        id: id_num,
                        title : $('#title').val(),
                        due_date: $('#dueDate').val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                success: function() {
                    location.reload();          
                }
                });
        } else {
            setTimeout(function() {
                $('.message2').text("Cannot update to empty task.").delay(1000).fadeOut();         
            });
        }
    });
});

// Once the delete button is clicked, calls AJAX POST request, which sends the id over to /delete
$(document).ready(function() {
    $(document).on("click", ".delete", function(){
        var id_num = $(this).data('id');

        $.ajax({
            type:'POST',
            url: 'delete/',
            data: {
                    id: id_num,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
            success: function() {
                setTimeout(function() {
                    $('.message').text("Completed").delay(100).fadeOut(function(){
                        location.reload();
                    });
                   });           
            }
            });
    });
});
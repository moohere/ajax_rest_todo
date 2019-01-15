function addTask(){
    $.ajax({
    type:'POST',
    url: 'add/',
    data: {
            title : $('#title').val(),
            due_date: $('#dueDate').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
}

function editTask(){
    var curTitle = $('#title').val()
    $(".edit").click(function(){
        $("#title").val(curTitle);
      });

    $.ajax({
    type:'POST',
    url: 'edit/',
    data: {
            id: $('.delete').val(),
            title : $('#title').val(),
            due_date: $('#dueDate').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
}

function deleteTask(){
    $.ajax({
    type:'POST',
    url: 'delete/',
    data: {
            id: $('.delete').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
}
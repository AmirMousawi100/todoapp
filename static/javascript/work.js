
$('textarea').text = $('textarea').val().length
$('textarea').keyup(function(){

    var characterCount = $(this).val().length,
        current = $('#current_textarea'),
        maximum = $('#maximum_textarea'),
        theCount = $('#the_count2');
    
    current.text(characterCount)    

    if(characterCount < 70){
        current.css('color', '#9042f5');
    }else if(characterCount > 70 && characterCount < 90){
        current.css('color', '#f542d4');
    } else if(characterCount > 90 && characterCount < 100){
        current.css('color', '#f54242')
    }
})

$('#todo_title').keyup(function(){

    var characterCount = $(this).val().length,
        current = $('#current'),
        maximum = $('#maximum'),
        theCount = $('#the_count1');
    
    current.text(characterCount)    

    if(characterCount < 70){
        current.css('color', '#9042f5');
    }else if(characterCount > 70 && characterCount < 90){
        current.css('color', '#f542d4');
    } else if(characterCount > 90 && characterCount < 100){
        current.css('color', '#f54242')
    }
})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // function showForm(){
        //     document.getElementById("list_div").style.display="none";
        //     document.getElementById("form_div").style.display="block";
        // }

        // function showList(){
        //     document.getElementById("list_div").style.display="block";
        //     document.getElementById("form_div").style.display="none";
        // } 

        // function testAjax(){
        //     fetch("/app1/testdata")
        //     .then(response => response.json())
        //     .then(data => console.log(data))
        // }

        console.log('javascript from static file')

        
        function showTodoDetals(id){
            // console.log(document.getElementById("div_todo_details").style.display)
            // if(document.getElementById("div_todo_details").style.display == "none"){
            //     document.getElementById("div_todo_details").style.display="block";
            // }else {
            //     document.getElementById("div_todo_details").style.display="none";
            // }
            console.log(id)
            window.open("my-activity/display/"+id, "_self")
            
        }

        function testAjax(){
            fetch("/app1/testdata", {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                }
            })
            .then(response => response.json())
            .then(data => {
            console.log(data);
            let c = data.context.length
            for(let count = 0 ; count < c ; count++){
                document.getElementById("p").innerText += data.context[count].username+"\n"
            }
            
            });
        }

        function deleteTodo(id){
            // fetch("/app1/my-activity/"+id, {
            //     method: "GET",
            //     headers: {
            //         "X-Requested-With": "XMLHttpRequest",
            //     }
            // })

            window.open("delete/"+id, "_self")
        }
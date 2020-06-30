$( document ).ready(function() {
    $(".edit_btn").on("click", function(){
        $(this).closest('.read_only').addClass('edit_enabled').removeClass('read_only')
    })
    $(".cancel_btn").on("click", function(){
        $(this).closest('.edit_enabled').addClass('read_only').removeClass('edit_enabled')   
    })
    
})
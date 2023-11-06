function addToCart(product,csrf){
    $.ajax({
        type: 'POST',
        url: '/cart/addtocart/',  
        data:{
            product: JSON.stringify(product),
            csrfmiddlewaretoken: csrf
        },
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': csrf
        },
        success: function(response) {
            // Handle the server's response here
            console.log(response);
        }
    });
}

function DeleteFromCart(csrf,id){
    $.ajax({
        type: 'DELETE',
        url: `/cart/del/${id}`,  
        data:{
            csrfmiddlewaretoken:csrf
        },
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': csrf
        },
        success: function(response) {
            console.log(response)
            location.reload()
        }
    });
}
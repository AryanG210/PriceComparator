function addToCart(product,csrf){
    $.ajax({
        type: 'POST',
        url: '/cart/addtocart/',  // Replace with the actual URL
        data:{
            product: JSON.stringify(product),
            csrfmiddlewaretoken:csrf
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
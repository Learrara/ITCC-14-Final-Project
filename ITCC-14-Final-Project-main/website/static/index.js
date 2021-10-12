    function deleteOrder(orderId) { 
        fetch("/delete-order", {
            method: "POST",
            body: JSON.stringify({ orderId: orderId }),
        }).then((_res) => {
            window.location.href = "/cart"
        })
        }
    
    function clearOrders(userId) { 
         fetch("/clear-order", {
            method: "POST",
            body: JSON.stringify({ userId: userId }),
        }).then((_res) => {
            window.location.href = "/cart"
        })
        }

        
    function addOrder(item) {   
        document.getElementById("test").innerHTML = item;
        fetch("/add_order", { 
            method: "POST",
            body: JSON.stringify({ itemName: item})
        }).then((_res) => {
            window.location.href = "/cart"
        })
       }
   
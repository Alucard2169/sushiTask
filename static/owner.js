const orderList = document.getElementById('orderList');
const userRoute = document.getElementById("gotoUser")

async function fetchOrders() {
    const response = await fetch('http://localhost:5000/api/orders');
    const orders = await response.json();
    orderList.innerHTML = ""
    orderList.innerHTML = orders.map(order => `
        <div>
            <h3>Order #${order.id}</h3>
            <p>Sushi A: ${order.sushi_a_count}</p>
            <p>Sushi B: ${order.sushi_b_count}</p>
            <p>Total Price: £${order.total_price}</p>
            <p>Discount Applied: ${order.discount_applied}%</p>
            <p>Order Time: ${new Date(order.order_time).toLocaleString()}</p>
        </div>
    `).join('');
}

fetchOrders();


setInterval(fetchOrders, 30000);


userRoute.addEventListener('click',()=>{
    location.assign("/")
})
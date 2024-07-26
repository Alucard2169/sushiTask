const customerOrderForum = document.getElementById("orderForm")

const ownerPageRoute = document.getElementById('gotoOwner')


customerOrderForum.addEventListener('submit', async (e) => {
    e.preventDefault();
    console.log(e.sushiA)
    const sushiA = parseInt(document.getElementById('sushiA').value);
    const sushiB = parseInt(document.getElementById('sushiB').value);

    const response = await fetch('http://localhost:5000/api/add-to-cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sushi_a_count: sushiA,
            sushi_b_count: sushiB
        }),
    });



    const result = await response.json();
    document.getElementById('orderSummary').innerHTML = `
        Order placed successfully!<br>
        Total price: £${result.total_price.toFixed(2)}<br>
        Discount applied: ${result.discount.toFixed(2)}%
    `;
});



ownerPageRoute.addEventListener("click", () => {
    location.assign("/susan")
})


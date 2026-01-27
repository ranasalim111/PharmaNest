let cart = [];
let total = 0;

function showCategory(cat) {
    let items = document.getElementsByClassName("item");
    for (let i=0;i<items.length;i++) {
        items[i].style.display =
            (cat==="all" || items[i].classList.contains(cat)) ? "block":"none";
    }
}

function searchMedicine() {
    let val = document.getElementById("search").value.toLowerCase();
    let items = document.getElementsByClassName("item");
    for (let i=0;i<items.length;i++) {
        items[i].style.display =
            items[i].innerText.toLowerCase().includes(val) ? "block":"none";
    }
}

function addToCart(name, price) {
    cart.push({name, price});
    total += price;
    document.getElementById("cartCount").innerText = cart.length;
    alert(name + " added to cart");
}

function openCart() {
    let list = document.getElementById("cartItems");
    list.innerHTML = "";
    cart.forEach(item => {
        let li = document.createElement("li");
        li.innerText = item.name + " - $" + item.price;
        list.appendChild(li);
    });
    document.getElementById("totalPrice").innerText = total;
    document.getElementById("cartModal").style.display = "block";
}

function closeCart() {
    document.getElementById("cartModal").style.display = "none";
}

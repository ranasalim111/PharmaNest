<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PharmaNest</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>PharmaNest</h1>
    <p>Your Trusted Online Pharmacy</p>
</header>

<nav>
    <a onclick="showCategory('all')">Home</a>
    <a onclick="showCategory('medicine')">Medicine</a>
    <a onclick="showCategory('baby')">Baby & Family</a>
    <a onclick="showCategory('skin')">Skin & Hair Care</a>
    <span class="cart-btn" onclick="openCart()">🛒 Cart (<span id="cartCount">0</span>)</span>
</nav>

<input type="text" id="search" placeholder="Search medicine..." onkeyup="searchMedicine()">

<div class="products">

    <div class="item medicine">
        <h3>Paracetamol</h3>
        <p>$3</p>
        <button onclick="addToCart('Paracetamol',3)">Add to Cart</button>
    </div>

    <div class="item medicine">
        <h3>Ibuprofen</h3>
        <p>$5</p>
        <button onclick="addToCart('Ibuprofen',5)">Add to Cart</button>
    </div>

    <div class="item baby">
        <h3>Baby Syrup</h3>
        <p>$4</p>
        <button onclick="addToCart('Baby Syrup',4)">Add to Cart</button>
    </div>

    <div class="item baby">
        <h3>Diapers</h3>
        <p>$8</p>
        <button onclick="addToCart('Diapers',8)">Add to Cart</button>
    </div>

    <div class="item skin">
        <h3>Face Cream</h3>
        <p>$6</p>
        <button onclick="addToCart('Face Cream',6)">Add to Cart</button>
    </div>

    <div class="item skin">
        <h3>Hair Shampoo</h3>
        <p>$7</p>
        <button onclick="addToCart('Hair Shampoo',7)">Add to Cart</button>
    </div>

</div>

<!-- Cart Modal -->
<div id="cartModal">
    <div class="cart-content">
        <h2>Shopping Cart</h2>
        <ul id="cartItems"></ul>
        <p><strong>Total: $<span id="totalPrice">0</span></strong></p>
        <button onclick="closeCart()">Close</button>
    </div>
</div>

<footer>
    <p>© 2026 PharmaNest</p>
</footer>

<script src="script.js"></script>
</body>
</html>

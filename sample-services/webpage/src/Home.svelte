<script>
    import { Link } from "svelte-routing";
    import { Button, Card, Container, Row, Col } from "sveltestrap";

    import gsap from "gsap";

    let bananas = 20; // Default value
    let oranges = 10; // Default value

    $: if (bananas < 1) bananas = 1;
    $: if (bananas > 500) bananas = 500;
    $: if (oranges < 1) oranges = 1;
    $: if (oranges > 500) oranges = 500;

    function makeItRain() {
        const n_bananas =
            parseInt(document.querySelector("#swap-currency-input").value) ||
            bananas;
        const n_oranges =
            parseInt(document.querySelector("#swap-currency-output").value) ||
            oranges;

        console.log(document.querySelector("#swap-currency-input"));
        console.log(n_bananas, n_oranges);
        makeItRainBananas(n_bananas);
        makeItRainOranges(n_oranges);
    }

    function makeItRainOranges(n_oranges) {
        if (n_oranges < 1) {
            n_oranges = 1;
        }
        const totalOranges = n_oranges;
        const orangesContainer = document.querySelector(".fruit-container");

        for (let i = 0; i < totalOranges; i++) {
            const orange = document.createElement("div");
            orange.innerText = "🍊";
            orange.style.position = "absolute";
            orange.style.left = `${Math.random() * 100}vw`;
            orange.style.top = `-2rem`;

            orangesContainer.appendChild(orange);

            gsap.to(orange, {
                y: "100vh",
                duration: Math.random() * 2 + 3,
                ease: "none",
                onComplete: () => orange.remove(),
            });
        }
    }

    function makeItRainBananas(n_bananas = 20) {
        if (n_bananas < 1) {
            n_bananas = 1;
        }
        const totalBananas = n_bananas;
        const bananasContainer = document.querySelector(".fruit-container");

        for (let i = 0; i < totalBananas; i++) {
            const banana = document.createElement("div");
            banana.innerText = "🍌";
            banana.style.position = "absolute";
            banana.style.left = `${Math.random() * 100}vw`;
            banana.style.bottom = `-2rem`; // Changed from top to bottom to make bananas start from the bottom

            bananasContainer.appendChild(banana);

            gsap.to(banana, {
                y: "-100vh", // Changed direction to make bananas go upwards
                duration: Math.random() * 2 + 3,
                ease: "none",
                onComplete: () => banana.remove(),
            });
        }
    }
</script>

<div class="fruit-container"></div>
<div class="swap-wrapper">
    <div class="swap-header">
        <h2>Fruit</h2>
    </div>
    <div class="swap-section">
        <div id="swap-currency-input-div" class="input-panel">
            <div class="input-container">
                <div class="label">You pay</div>
                <div class="input-row">
                    <input
                        class="numerical-input"
                        id="swap-currency-input"
                        type="number"
                        placeholder="20"
                        min="1"
                        max="500"
                        bind:value={bananas}
                    />
                    <button class="currency-select-button">Banana(s)</button>
                </div>
            </div>
        </div>
    </div>
    <div class="swap-section output-section">
        <div id="swap-currency-output-div" class="input-panel">
            <div class="input-container">
                <div class="label">You receive</div>
                <div class="input-row">
                    <input
                        class="numerical-input"
                        id="swap-currency-output"
                        type="number"
                        placeholder="10"
                        min="1"
                        max="500"
                        bind:value={oranges}
                    />
                    <button class="currency-select-button">Orange(s)</button>
                </div>
            </div>
        </div>
    </div>
    <div class="action-section">
        <button class="connect-wallet-button" on:click={makeItRain}
            >Exchange</button
        >
    </div>
</div>

<style>
    .fruit-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 9999;
    }
</style>

<script>
	import { Router, Route, Link } from "svelte-routing";
	import Home from "./Home.svelte";
	import About from "./About.svelte";
</script>

<Router>
	<nav class="main-nav-bar">
		<Link to="/" class="page-link">Home</Link>
		<Link to="/about" class="page-link">About</Link>
	</nav>

	<main>
		<Route path="/" component={Home} />
		<Route path="/about" component={About} />
	</main>
</Router>

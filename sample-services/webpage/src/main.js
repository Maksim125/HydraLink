import App from './App.svelte';
import { Router, Route, Link } from 'svelte-routing';
import './global.css';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;

new Router({
	target: document.body,
	routes: [
		{ path: '/', component: App },
	]
})
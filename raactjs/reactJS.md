# What is React?
React is a JavaScript library for building user interface using reusable components.It uses a declarative programming model where we describe what the UI should look like for a given state, and React takes care of updating the DOM when the state changes

-> React primarly uses a component-based architecture, one-way data flow, state management through hooks, and a reconciliation process to efficiently update the UI.

DOM(Document Object Model): The DOM is a tree-like representation of your HTML page that the browser creates
For example, if your HTML is:

<div>
  <h1>Hello</h1>
  <button>Click Me</button>
</div>

The browser represents it roughly like:

Document
 └── div
      ├── h1
      │    └── "Hello"
      └── button
           └── "Click Me"

JavaScript can interact with this DOM:

document.querySelector("h1").textContent = "Hello Fasi";
The browser then changes what you see on the page.

So what does React do?
Suppose you have:

function App() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}

Initially:

0

When you click:

1

You don't manually write:
document.querySelector("button").textContent = "1";
Instead, you tell React:
"When count changes, I want the UI to show the new count."
React determines what changed and updates the necessary part of the DOM.
That's what this sentence means:
React takes care of updating the DOM when that state changes.

# Why use React instead of plain JavaScript
In plain JavaScript we manually manipulate DOM elements whenever application data changes.In React, the UI is derived from state.When state changes, React determines what needs to change and updates the DOM.
For example, instead of:

document.getElementById("count").innerText = count;

React:

function Counter() {
  const [count, setCount] = useState(0);


  return <h1>{count}</h1>;
}

When count changes, React updates the UI.

# What is SPA(Single Page Application)
Instead of requesting an entirely new HTML page from the server for every navigation.
Traditional Website
/browser -> GET /home -> Server returns home.html 
click profile
GET /profile -> Server returns profile.html

React commonly works like:

Browser -> React application loaded -> Home component 
click profile -> Ract Router -> Profile Component
The application dynamically updates portions of the page
Benifits
1. Faster navigation
2. Better UX
3. Reusable components
4. Reduced full-page reloads

# What is JSX
JSX allows us to write HTML-like syntax inside JavaScript
Example:

const name = "Fasi";
return <h1>Hello {name}</h1>;

Browsers don't understand JSX directly.
It gets transformed into JavaScript.

Conceptually:
<h1>Hello</h1>

becomes something similar to:

React.createElement("h1", null, "Hello");
Modern React tooling handles this transformation.

# JSX vs HTML
Some differences:

className="container"

instead of:

class="container"

Events:

onClick={handleClick}

instead of:

onclick="handleClick()"

JavaScript values:

<h1>{username}</h1>

Styles:

<div style={{ backgroundColor: "red" }}>

# What is React component?
React applications are built using components.

function UserCard() {
  return <h2>User</h2>;
}

Usage:

<UserCard />

A component should ideally have one clear responsibility.

For example:

App
 ├── Navbar
 ├── Sidebar
 ├── UserList
 │     ├── UserCard
 │     ├── UserCard
 │     └── UserCard
 └── Footer

This makes the UI reusable and maintainable.

# Functional vs Class Components
Older React:

class Counter extends React.Component {
  state = {
    count: 0
  };
}

Modern React primarily uses functional components:

function Counter() {
  const [count, setCount] = useState(0);

  return <div>{count}</div>;
}

**Class components use lifecycle methods and this, while functional components use hooks such as useState and useEffect. Modren React applications generally prefer functional components because they're simpler and support reusab,e stateful logic through hooks.

# What are props?
Props mean properties. They pass data from parent -> child

function User({ name }) {
  return <h1>{name}</h1>;
}

function App() {
  return <User name="Fasi" />;
}
Flow:

App
 |
 | name="Fasi"
 ↓
User

Props are read-only.

You should not do:

props.name = "Ahmed";

# State vs Props
Props                    State
Passed from parent       Managed by Component
Read-only                can be updated
External input           Internal data
Parent controls it       Component controls it
Example:

function Counter({ initialCount }) {
  const [count, setCount] = useState(initialCount);
}

initialCount → prop

count → state

# What is State?
State is data that React remembers between renders
const [count, setCount] = useState(0);
Here count is the current value
setCount updates it.
0 is initial state

# What happends when the state changes
Suppose setCount(count+1)
React roughly does 
setCount() -> Schedules state update -> Component function runs again -> New React element tree produced -> React compares previous and new trees -> Necessary DOM changes are commited -> Browser displays update UI

Re-render does not mean the entire DOM is recreated
The component function may execute again, but React determines what actuall DOM updates are needed.





# Client Side Routing

### SWBATs:

- [ ] Review the difference between server-side and client-side routing
- [ ] Observe a refactor to include client-side routing using React Router V5
- [ ] Explain what a nested route is
- [ ] Observe how to handle nested client-side routes

## Deliverables

#### 1. Install and setup react router

- React Router has been updated to V6 but V5 is used in the curriculum.

- To install V5 run this command: `npm install react-router-dom@5.3.0` otherwise, V6 will install by default

- Wrap the `App` component inside of the `BrowserRouter` component that will be imported from the `react-router-dom` library

#### 2. Use Switch and Route to set up initial routes so we can conditionally render components based on URL

- Import the `Switch` component from the `react-router-dom` library and wrap the components designated for routing

- Import the `Route` component from the `react-router-dom` library and wrap each individual component designated for routing

  - Provide the `path` prop to the `Route` component to create a URL path associated with the component

- Demonstrate each route in the browser to confirm desired expectation is occuring

- Demonstrate the use of the `exact` prop passed to the `Route` component

#### 3. Add navigation to the application using the `Link` and `NavLink` components

- Convert any html anchor tags to `Link` or `NavLink`

- Demonstrate the difference between `Link` and `NavLink`

#### 4. Create a nested route for the project show page inside of the `ProjectList` component



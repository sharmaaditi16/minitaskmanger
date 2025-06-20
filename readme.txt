1.Why did you choose this project structure?
ans: The project structure is simple , file name and variable naming conventions are self sufficient, extendable and requires limited knowledge transfer to other team members so it gets easy for someone viewing the project to grasp the prooject easily.

2.How did you separate frontend and backend concerns ?
ans:Backend and frontend is designed with business case/requirement consideration. Now if our client requires web application, mobile application or even SAS. APIs should be complete in terms of business logic and loosely coupled to be consumed by any client.

3. How would you handle errors and edge cases ?
ans:1. Handle basic error conditions/validations such as empty string value, null values 
    2. Use Try, Catch block wherever necessary
    3. From API, proper Http status should be sent along with response

4.What security features would you add in production?
ans:1. Add CSRF protection to avoid misuse of APIs
    2. Add authentication in APIs

5.What would you improve if you had 1 day ?
ans:1. Improve error handling & validations
    2. Include basic authentication in UI & APIs 
    3. Improve UI with adding better designed components and API responses in UI
    4.I’ll integrate Tailwind CSS and replace Bootstrap. I’ve integrated with Boostrap since I’m familiar.
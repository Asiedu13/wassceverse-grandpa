import Home from "./views/Home.js";
// import About from "./views/About.js";
const navigateTo = (url) => {
  history.pushState(null, null, url);
  router();
};

const router = async () => {
  const routes = [
    { path: "/", view: Home },
    // { path: "/about", view: About },
    // { path: "/posts", view: () => console.log("Main posts") },
  ];

  const potentialMatches = routes.map((route) => {
    return {
      route,
      isMatch: location.pathname === route.path,
    };
  });
  console.log(potentialMatches);
  const findMatch = potentialMatches.find(
    (potentialMatch) => potentialMatch.isMatch
  );

  console.log(findMatch);

  // Update the view
  let view = new findMatch.route.view();
  console.log(view);

  document.querySelector("#app").innerHTML = await view.getHTML();
};

window.addEventListener('popstate', router)

document.addEventListener("DOMContentLoaded", async () => {
  document.body.addEventListener("click", (e) => {
    if (e.target.matches("[data-link]")) {
      e.preventDefault();
      navigateTo(e.target.href);
    }
  });
  router();
});

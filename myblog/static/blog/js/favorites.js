function getCookie(name) {
  let cookieVal = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieVal = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieVal;
}

document.querySelectorAll(".star-button").forEach((star) => {
  star.addEventListener("click", async () => {
    const isFavorite = star.classList.contains("filled");
    const id = star.dataset.itemId;
    const type = star.dataset.type;

    const csrfToken = getCookie("csrftoken");
    if (csrfToken === null) {
      throw new Error(`No CSRF token found!`);
    }

    const response = await fetch("/blog/favorite/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        operation: isFavorite ? "remove" : "add",
        type: type,
        id: id,
      }),
    });

    if (response.ok) {
      star.classList.toggle("filled");
      star.classList.toggle("empty");
    } else {
      console.log(`csrf token: ${getCookie("csrftoken")}`);
      throw new Error(`Response status: ${response.status}`);
    }
  });
});

function getUserDetails(user) {
  fetch('https://proxy.jaydendev.repl.co/api.scratch.mit.edu/users/' + user)
    .then(res => res.json())
      .then(data => {
          console.log(data)
          const { profile.images.90x90 } = data;
          console.log(profile.images.90x90)
        });
}

function doSomethingWithUsername() {
  let getUser = document.querySelector('#userInput').val
  let userNameTitle = document.querySelector('.user-title')
  userNameTitle.innerText = getUser
}

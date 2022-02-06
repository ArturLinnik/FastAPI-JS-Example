$("#my_form").submit(async function(e) {
	e.preventDefault();

	form = document.getElementById("my_form")

	username =form.username.value
	password =form.password.value

	const response = await fetch("http://localhost:8000/api/v1/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({
			username: username,
			password: password
		})
	})
		.then(res => {
			return res.json()
		})
		.then(data => {
            success = data["success"];
            if (success == false) {
                alert("BAD")
                return false;
            } else {
                alert("Successful")
                fetch("http://localhost:8000/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                })
                    .then(res => {
                        console.log(res.json())
                        this.submit()
                    })
            }
		})
})
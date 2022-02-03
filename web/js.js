function send() {

    username = $("#username").val()
    password = $("#password").val()

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
            return res.json()
        })
        .then(data => {
            success = data["success"];

            if (success == false) {
                alert("User or password not valid");

            } else {

                alert("Succesful")

                $(function () {
                // Grab the template script
                var theTemplateScript = $("#address-template").html();

                // Compile the template
                var theTemplate = Handlebars.compile(theTemplateScript);

                // Define our data object
                var context={
                    "username": username,
                    "password": password
                };

                // Pass our data to the template
                var theCompiledHtml = theTemplate(context);

                // Add the compiled html to the page
                $('.content-placeholder').html(theCompiledHtml);
                });
            }
        })
}
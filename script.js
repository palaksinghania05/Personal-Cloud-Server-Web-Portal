// function where main operation is performed
function miniproject() {
    
    // store input value in a variable
    var input = document.getElementById("in").value;
    console.log(input);
    
    // used to exchange data with a web server behind the scenes
    const httpRequest = new XMLHttpRequest();
    
    // send the request to specified server
    httpRequest.open("GET","http://192.168.225.20/cgi-bin/project.py?x="+input,true);
    httpRequest.send();
    
    httpRequest.onload = function() {
        // What to do when the response is ready
        if (httpRequest.status == 200) {
            var output = httpRequest.responseText;
        } else {
            var output = input;
        }
        document.getElementById("display").innerHTML = output;
    }
}

// to go back to home page
function goBack() {
    window.history.back()
}

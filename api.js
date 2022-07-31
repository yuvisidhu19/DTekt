chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let current_url = tabs[0].url;
    
    // use `url` here inside the callback because it's asynchronous!

    // var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
    // var theUrl = "http://127.0.0.1:5000";
    // xmlhttp.open("POST", theUrl);
    // xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    // let data = xmlhttp.send(JSON.stringify({ "url": current_url}));
    
    // const test = document.getElementById('test');
    // test.innerHTML = data;

    // import fetch from "node-fetch";
    const test = document.getElementById('test');
    test.innerHTML = "Fetching data...";

    let URL = "http://127.0.0.1:5000";
    const data = {
    "url": current_url
    };
    // Send a post request
    fetch(URL, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    .then(
        function(u) { return u.json(); }
    )
    .then(
        function(json) {
        
            if (json["flag"] == 1) {
                test.innerHTML = "Invalid website or No reviews available";
            }
            else {
                test.innerHTML = "Applying ML model...";
                URL = "http://127.0.0.1:7000";

                fetch(URL, {
                    method: "POST",
                    body: JSON.stringify({"name": json["test"]}),
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                    })
                    .then(
                        function(u) { return u.json(); }
                    )
                    .then(
                        function(json) {
                            test.innerHTML = "Authenticity score is " + json["val"];

                            let circularProgress = document.querySelector(".circular-progress"),
                            progressValue = document.querySelector(".progress-value");

                            var authenticity_score=Math.round(json["val"]);

                            let progressStartValue = 0,    
                            progressEndValue = authenticity_score,    
                            speed = 10;

                            let progress = setInterval(() => {

                            progressValue.textContent = `${progressStartValue}%`
                            circularProgress.style.background = `conic-gradient(#febd69 ${progressStartValue * 3.6}deg, #ededed 0deg)`

                            if(progressStartValue == progressEndValue){
                                clearInterval(progress);
                            }    
                            progressStartValue++;
                            }, speed);
                        }
                    )
            }
        }
    )
});




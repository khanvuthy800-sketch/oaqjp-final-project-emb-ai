let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Parse the JSON response
                try {
                    const data = JSON.parse(xhttp.responseText);
                    if (data.error) {
                        document.getElementById("system_response").innerHTML = 
                            "<span style='color: red;'>" + data.error + "</span>";
                    } else if (data.response) {
                        document.getElementById("system_response").innerHTML = data.response;
                    } else {
                        document.getElementById("system_response").innerHTML = 
                            "<span style='color: red;'>Unexpected response format</span>";
                    }
                } catch (e) {
                    document.getElementById("system_response").innerHTML = 
                        "<span style='color: red;'>Error parsing response</span>";
                }
            } else if (this.status == 400) {
                // Handle 400 Bad Request errors
                try {
                    const data = JSON.parse(xhttp.responseText);
                    document.getElementById("system_response").innerHTML = 
                        "<span style='color: red;'>" + data.error + "</span>";
                } catch (e) {
                    document.getElementById("system_response").innerHTML = 
                        "<span style='color: red;'>Invalid text! Please try again!</span>";
                }
            } else {
                // Handle other errors
                document.getElementById("system_response").innerHTML = 
                    "<span style='color: red;'>Error: " + this.status + " - Please try again</span>";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
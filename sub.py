import requests

var options = {
    method: 'POST',
    / ** & wait = true for getting the submission result after submitting the code automatically * /
    url: "http://sntc.iitmandi.ac.in:3000/submissions/?base64_encoded=false&wait=true",
    headers: {
            "cache-control": "no-cache",
            "Content-Type": "application/json"
    },
    body: {
        "source_code": req.body.src,
        "language_id": parseInt(req.body.lang),
        "stdin": req.body.stdin,
        "cpu_time_limit": 5 // time limit to 5 sec for the IDE
    },
    json: true
}
console.log(options)
request(options, function(err, result, body) {
    res.send(body)
    console.log(res)
})

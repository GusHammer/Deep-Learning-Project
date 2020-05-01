function submit(){
	console.log("wjwjw");
	var data = new FormData();
	data.append('file', document.getElementById("file").files[0]);
	$.ajax({
		url: 'http://localhost:5000/api/v1/predict/sample',
		type: 'POST',
		contentType: false,
		cache: false,
		processData: false,
		data: data,
		success: function (data) {
			window.location.href = "answer.html?answer=" + data;
		}
	});
}
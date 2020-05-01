function pageLoaded(){
	var params = new URLSearchParams(window.location.search);
	document.getElementById("answer").innerHTML = params.get("answer")
}
window.onload = pageLoaded;
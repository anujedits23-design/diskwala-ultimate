async function go(){
    let link = document.getElementById("link").value;

    if(!link){
        document.getElementById("result").innerHTML = "❌ Enter link";
        return;
    }

    document.getElementById("result").innerHTML = "⏳ Processing...";

    let r = await fetch("/extract", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({link})
    });

    let d = await r.json();

    if(d.status){
        let final = "/fast?url=" + encodeURIComponent(d.direct);

        document.getElementById("result").innerHTML = `
            <button onclick="openVideo('${final}')">
                📥 Open Video
            </button>
        `;
    } else {
        document.getElementById("result").innerHTML = "❌ Failed";
    }
}

function openVideo(url){
    Telegram.WebApp.openLink(url);
}

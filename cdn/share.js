const options = {
    apiKey: "public_FW25c9NhWKQ2sboH2hhMf8eXQd4j",
    maxFileCount: 1
};
function upload() {
    Bytescale.UploadWidget.open(options).then(
        files => {
        const p = document.getElementById("par")
        const fileUrls = files.map(x => x.fileUrl).join("\n");
        const success = fileUrls.length === 0
            ? "No file selected."
            : `${fileUrls}`;
        p.innerHTML = success;
        getNewUrl()
        },
        error => {
        alert(error);
        }
    );
}
function getNewUrl() {
const p = document.getElementById("par")
const url = 'https://spoo.me/';
const data = new URLSearchParams();
data.append('url', p.innerHTML);

const xhr = new XMLHttpRequest();
xhr.open('POST', url, true);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.setRequestHeader('Accept', 'application/json');

xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
            r = xhr.responseText.replace("short_url", "url").toString()
            p.innerHTML = r
        } else {
            console.error(`HTTP error! Status: ${xhr.status}`);
        }
    }
};

xhr.send(data);
}

function getSocialLinks(q) {
    var twitter = "https://twitter.com/intent/tweet?url=" + q
    var facebook = "https://www.facebook.com/sharer/sharer.php?u=" + q
    var telegram = "https://t.me/share/url?url=" + q
    var whatsapp = "https://api.whatsapp.com/send?text=" + q
    var reddit = "https://www.reddit.com/submit?url=" + q
    var snapchat = "https://snapchat.com/scan?attachmentUrl=" + q
    document.write("<head><link rel='stylesheet' href='https://grugraphics.vercel.app/cdn/style.css'></head>")
    document.write("<h3>GRU Sharing Platform</h3>")
    document.write("<div><a href='" + twitter + "'>Twitter</a></div>")
    document.write("<div><a href='" + facebook + "'>Facebook</a></div>")
    document.write("<div><a href='" + telegram + "'>Telegram</a></div>")
    document.write("<div><a href='" + whatsapp + "'>WhatsApp</a></div>")
    document.write("<div><a href='" + reddit + "'>Reddit</a></div>")
    document.write("<div><a href='" + snapchat + "'>Snapchat</a></div>")
}
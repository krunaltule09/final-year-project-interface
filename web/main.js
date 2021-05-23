const loading=document.querySelector(".loading")
const caption_text_label=document.querySelector(".caption-text");


const file=document.getElementById("file")

file.addEventListener("change",()=>{
    loading.classList.add("active")
    caption_text_label.classList.remove("active")
})

var loadFile = function(event) {

    // console.log(event);

    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    loading.classList.add("active")
    caption_text_label.classList.remove("active")
    eel.dummy(event.target.value)(setCaption);

};


function setCaption(caption) {
    var cc = document.querySelector(".caption");
    loading.classList.remove("active")
    caption_text_label.classList.remove("active")

    cc.innerText = `${caption}`;
}
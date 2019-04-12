// window.onload = function(event) {
//     body = document.body;
//     html = document.documentElement;
//     var footer = document.querySelector('footer');
//     footer.style.position = "absolute";
//     footer.style.left = x_pos+'px';
//     footer.style.top = y_pos+'px';
// }
window.onresize = function(event) {
    resizeAll();
};

window.onload = function(event) {
    resizeAll();
}

function resizeAll(){
    var thumbWidth = document.getElementsByClassName('product-thumb')[0].offsetWidth;
    $('.product-thumb').height(thumbWidth + 'px')
}
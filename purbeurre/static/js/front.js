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
    if($('.product-thumb')[0]){
        var thumbWidth = document.getElementsByClassName('product-thumb')[0].offsetWidth;
        $('.product-thumb').height(thumbWidth + 'px')
    }
    // console.log('.documentElement.scrollHeight = ' + document.documentElement.scrollHeight);
    // console.log('.body.clientHeight = ' + document.body.clientHeight);
    // console.log('window.outerHeight = ' + window.outerHeight);
    if (document.documentElement.scrollHeight > document.body.clientHeight + 41){
        document.querySelector('footer').style.position = 'relative'
    }else{
        document.querySelector('footer').style.position = 'absolute'
    }
    if (document.documentElement.scrollWidth < 480){
        $('.fa-arrow-right').removeClass('fa-4x').addClass('fa-2x')
        $('.fa-trash-alt').removeClass('fa-4x').addClass('fa-2x')
    }else{
        $('.fa-arrow-right').removeClass('fa-2x').addClass('fa-4x')
        $('.fa-trash-alt').removeClass('fa-2x').addClass('fa-4x')
    }
}
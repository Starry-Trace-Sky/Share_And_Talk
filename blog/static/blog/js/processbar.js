var navbar = document.getElementsByTagName('nav')[0];
var navbar_style = getComputedStyle(navbar);
var navbar_height = navbar_style.height;
var progress = document.getElementById('progress');

document.addEventListener('scroll', function (e) {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop; // 已经读过被卷起来的文档部分
    var scrollHeight = document.documentElement.scrollHeight // 文档总高度
    var clientHeight = document.documentElement.clientHeight // 窗口可视高度
    document.getElementById('read_pro_inner').style.width = +(scrollTop / (scrollHeight - clientHeight)).toFixed(2) * 100 + '%'
    progress.style.top = navbar_height
})

window.addEventListener('resize', function () {
    console.log('浏览器窗口大小已更改');
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop; // 已经读过被卷起来的文档部分
    var scrollHeight = document.documentElement.scrollHeight // 文档总高度
    var clientHeight = document.documentElement.clientHeight // 窗口可视高度
    document.getElementById('read_pro_inner').style.width = +(scrollTop / (scrollHeight - clientHeight)).toFixed(2) * 100 + '%'
    progress.style.top = navbar_style.height
})

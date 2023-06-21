/* var shareul = document.getElementById('shareul');

var sharelink = shareul.getElementsByTagName("a");

for(var i = 0;i < sharelink.length;i++) {
    sharelink[i].addEventListener('click',function(){
        var url = window.location.href;

        // 创建一个临时文本域
        var temp = document.createElement("textarea");
        temp.style.position = "absolute";
        temp.style.left = "-1000px";
        temp.value = url;
        document.body.appendChild(temp);

        // 选中临时文本域中的内容并复制到剪切板
        temp.select();
        document.execCommand("copy");

        // 移除临时文本域
        document.body.removeChild(temp);

        // 弹出提示框
        var $toast = $('#toastShare');
        $toast.toast({
          delay: 10000
        });
        $toast.toast('show');
        
        setTimeout(function() {
          $toast.toast('hide');
        }, 5000);

        return false;
            })
}
*/

var share_area = document.getElementsByClassName('share-area')[0]
var sharelink = share_area.getElementsByTagName('ul')[0]
sharelink.addEventListener('click', function (event) {
    var url = window.location.href;

    // 创建一个临时文本域
    var temp = document.createElement("textarea");
    temp.style.position = "absolute";
    temp.style.left = "-1000px";
    temp.value = url;
    document.body.appendChild(temp);

    // 选中临时文本域中的内容并复制到剪切板
    temp.select();
    document.execCommand("copy");

    // 移除临时文本域
    document.body.removeChild(temp);

    // 弹出提示框
    var $toast = $('#toastShare');
    $toast.toast({
        delay: 10000
    });
    $toast.toast('show');

    setTimeout(function () {
        $toast.toast('hide');
    }, 5000);

    return false;
})

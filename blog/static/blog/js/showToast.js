$(document).ready(function () {
    var $toast = $('#toastt');
    $toast.toast({
        delay: 10000
    });
    $toast.toast('show');

    setTimeout(function () {
        $toast.toast('hide');
    }, 5000);

})
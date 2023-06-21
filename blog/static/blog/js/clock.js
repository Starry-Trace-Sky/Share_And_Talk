function showTime() {

    //获取当前时间
    var currentDate = new Date();

    // 定义时间格式
    var year = currentDate.getFullYear(); // 年份
    var month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 月份，toString 和 padStart 可以保证一位数月份前面加 0
    var day = currentDate.getDate().toString().padStart(2, '0'); // 日，同样保证前面加 0
    var hour = currentDate.getHours().toString().padStart(2, '0'); // 小时，同样保证前面加 0
    var minute = currentDate.getMinutes().toString().padStart(2, '0'); // 分钟，同样保证前面加 0
    var second = currentDate.getSeconds().toString().padStart(2, '0'); // 秒，同样保证前面加 0

    //获取星期几
    var week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    var week_day = week[currentDate.getDay()]

    //console.log(week_day);

    // 拼接时间字符串
    var date = year + '-' + month + '-' + day + ' ' + week_day
    var time = hour + ':' + minute + ':' + second

    // 输出时间字符串
    //console.log(date + ' ' + time); // 输出格式化后的时间字符串

    const aside_clock = document.getElementsByClassName('aside-clock')

    for(let i = 0;i < aside_clock.length;i++){
        aside_clock[i].getElementsByClassName('date')[0].innerHTML = date
        aside_clock[i].getElementsByClassName('time')[0].innerHTML = time
    }
    //aside_clock.getElementsByClassName('date')[0].innerHTML = date
    //aside_clock.getElementsByClassName('time')[0].innerHTML = time

}

setInterval(showTime, 1000)
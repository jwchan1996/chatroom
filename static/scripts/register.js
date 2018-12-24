/**
 * Created by asus on 2017/6/4.
 */

$("#register").click(function () {

    if ($("#password").val() != ""&&$("#userName").val()!="") {

        $.post("http://pub.ngrok.jehoiada.cn/user/register", {
            userName: $("#userName").val(),
            password: $("#password").val()
        }, function (res) {
            console.log(JSON.stringify(res));
            if (res.status === 200) {
                window.location.href = "login.html";
            }
            else if (res.status === 411) {
                $("#tip").html("*该用户名已存在*");
            }
        });

    }else{
        $("#tip").html("*用户名和密码不能为空*");
    }

});


/**
 * Created by asus on 2017/6/4.
 */
var user = "";

$("#login").click(function () {

    if ($("#userName").val() != "" && $("#password").val() != "") {

        $.post("http://pub.ngrok.jehoiada.cn/user/login", {
            userName: $("#userName").val(),
            password: $("#password").val()
        }, function (res) {
            console.log(JSON.stringify(res));
            if (res.status === 200) {
                var userName = $("#userName").val();
                window.location.href = encodeURI("index.html?userName=" + userName);
            }
            else if (res.status === 413) {
                $("#tip").html("*该用户名不存在*");
            }else if(res.status===412){
                $("#tip").html("*用户密码错误*");
            }
        });
    } else {
        $("#tip").html("*用户名和密码不能为空*");
    }

});




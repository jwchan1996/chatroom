var webSocket = null;
var urlInfo = window.location.href;
var userName = urlInfo.split("?")[1].split("=")[1];
var chat_window = document.getElementById('chat-window');
var text;

//判断当前浏览器是否支持WebSocket
if ('WebSocket' in window) {
    webSocket = new WebSocket("ws://pub.ngrok.jehoiada.cn/socket?userName=" + decodeURI(userName));
}
else {
    alert('当前浏览器 Not support WebSocket');
}

//连接成功建立的回调方法
webSocket.onopen = function () {
    log("WebSocket连接成功");
};

//连接发生错误的回调方法
webSocket.onerror = function () {
    log("WebSocket连接发生错误");
};

//接收到消息的回调方法
webSocket.onmessage = function (event) {
    var message = JSON.parse(event.data);
    console.log(message);
    if (message.status === 200) {
        var html = "<ul>";
        for (var i = 0; i < message.userNames.length; i++) {
            html += "<li " + "id=" + message.userNames[i] + ">" + message.userNames[i] + "</li>";
        }
        html += "</ul>";
        $("#people-list").html(html);
    }
    else if (message.status === 211) {
        //有人加进来
        var t1 = new Date().toLocaleString();
        $("#chat-window").append("<p>" + t1 + "<br>系统提示：欢迎" + message.userName + "加入聊天室......</p>");
        var oldPeopleList = $("#people-list ul").html();
        var newPeopleList = oldPeopleList + "<li " + "id=" + message.userName + ">" + message.userName + "</li>";
        $("#people-list ul").html(newPeopleList);
        chat_window.scrollTop = chat_window.scrollHeight;
    }
    else if (message.status === 212) {
        //有人离开
        var t2 = new Date().toLocaleString();
        $("#chat-window").append("<p>" + t2 + "<br>系统提示：" + message.userName + "已离开聊天室......</p>");
        console.log(message.userName);

        $("#" + message.userName).remove();
        chat_window.scrollTop = chat_window.scrollHeight;

    }
    else if (message.status === 213) {
        //群发
        var userName = message.userName;
        var data = message.data;
        var date = new Date();
        var t = date.toLocaleString();
        $("#chat-window").append("<p>" + t + "<br>" + userName + "：&nbsp" + data + "</p>");

        chat_window.scrollTop = chat_window.scrollHeight;
    }
};

//连接关闭的回调方法
webSocket.onclose = function () {
    log("WebSocket连接关闭");
};

//监听窗口关闭事件，当窗口关闭时，主动去关闭websocket连接，防止连接还没断开就关闭窗口，server端会抛异常。
window.onbeforeunload = function () {
    webSocket.close();
};

//将消息显示在网页调试台上
function log(content) {
    console.log(content);
}

$("#send").click(function () {
    send();
});

$("#reset").click(function () {
    $("#chat-window").html("");
});

//监听回车
$('#text-input').bind('keyup', function (event) {
    if (event.keyCode === 13) {
        //回车发送
        send();
    } else if (event.keyCode === 17) {
        //Ctrl换行
        newline();
    }
});


//信息发送函数
function send() {
    var data = $('#text-input').val();
    var message = {
        "userName": decodeURI(userName),
        "data": data
    };
    webSocket.send(JSON.stringify(message));
    $("#text-input").val("");
}

//换行函数
function newline() {
    $("#text-input").val($("#text-input").val() + "\r\n");
    $("#text-input").focus();
}

$("#logo").click(function () {
    window.location.href = "login.html";
});





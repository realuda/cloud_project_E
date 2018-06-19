function showSignUp(){
            document.getElementById("sign-up-box").style.display="block";
        }/**
 * Created by user on 2016-01-19.
 * Mdificated by hs-kim on 2017-11-26.
 */

function signup(){
    var username = $("#Sign-up-Name").val();
    var passwd = $("#Sign-up-Password").val();
    var email = $("#Sign-up-Email").val();

    data={'username':username, 'passwd': passwd, 'email': email};
    json_data=JSON.stringify(data);

    $.ajax
   ({
      type: 'PUT',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: '/signup/',
      async: false,
      data: json_data,
      success: function(result){
         alert("회원가입 성공");
          location.reload();
      },
      statusCode:{
         409:function(msg){
            alert(msg.responseText);
         }
      }
   });
}


function signin(){
    var email = $("#inputEmail").val();
    var passwd = $("#inputPassword").val();

    data={'email':email, 'passwd': passwd};
    json_data=JSON.stringify(data);

    $.ajax
    ({
        type: 'POST',
        headers:
        {
           'Accept': 'application/json',
           'Content-Type': 'application/json'
        },
        url: '/signin/',
        async: false,
        data: json_data,
        success: function(result){
           location.reload();
        },
        statusCode:{
            404:function(msg){
                alert(msg.responseText);
            },
            400:function(msg){
                alert(msg.responseText);
            }
		}
    });
}


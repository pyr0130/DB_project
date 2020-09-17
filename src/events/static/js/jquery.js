function press(f)
{
  if(f.keyCode == 13)
  {
    login.submit(); //formname에 사용자가 지정한 form의 name입력
  }
}

//concert***************************************************************
$( window ).scroll( function() {
	if ( $( this ).scrollTop() > 200 ) {
		$( '.top' ).fadeIn();
	} else {
		$( '.top' ).fadeOut();
	}
} );



$( '.top' ).click( function() {
	$( 'html, body' ).animate( { scrollTop : 0 }, 400 );
	return false;
} );

$(document).ready(function(){
        // menu 클래스 바로 하위에 있는 a 태그를 클릭했을때
        $(".con_details>a").click(function(){
            var submenu = $("div.hide");

            // submenu 가 화면상에 보일때는 위로 보드랍게 접고 아니면 아래로 보드랍게 펼치기
            if( submenu.is(":visible") ){
                submenu.slideUp();
            }else{
                submenu.slideDown();
            }

            var submenu2 = $("form.searr");
            if( submenu2.is(":visible") ){
                submenu2.slideUp();
            }else{
                submenu2.slideDown();
            }
        });
    });

var cnt = 1;
function imgToggle(){
  if (cnt == 0){
    document.img2.src = "/static/images/mainconcert/detailsearch.png"
    cnt = 1;
  }else{
    document.img2.src = "/static/images/mainconcert/details2.png"
    cnt = 0;
  }
}


// concert_detail***********************************************

var state=0;

function ChangeImage(){
  if(state==0){
    document.img3.src="/static/images/concert_page/bookmark_yes.png"
    state=1;
  }
  else{
    document.img3.src="/static/images/concert_page/bookmark_no.png"
    state=0;
  }
}

function showPopup(code){
  window.open("/artpop/"+code,"추가 가수 정보","width=400, height=250, left=100, top=50")
}

// all_concert_sort**********************************************

function ChangeTextSort1(){
  $('#allc_sort').text("[ 종료 ]");
}
function ChangeTextSort2(){
  $('#allc_sort').text("[ 진행 ]");
}
function ChangeTextSort3(){
  $('#allc_sort').text("[ 예정 ]");
}
function ChangeTextSort4(){
  $('#allc_sort').text("[ 전체 ]");
}

// function ChangeTextSort5(){
//   $('#allc_sort').text("[ 연도별 ]");
// }
// function ChangeTextSort6(){
//   $('#allc_sort').text("[ 월별 ]");
// }


function ChangeTextSort8(){
  $('#allc_sort').text("[ 최다관심가수 ]");
}
function ChangeTextSort9(){
  $('#allc_sort').text("[ 최다관심공연 ]");
}

//****************************************
$(window).load(function () {

           $('#layer_ad').css({

               'position':'fixed',

               'bottom':0,

               'right':'20px',

               'padding':'10px',

               'font-size':'12px',

               'width':'250px',

               'height':'150px',

               'border-width':'1px 1px 0 1px',

               'border-color':'#aaaaaa',

               'border-style':'solid'

           });

           setInterval(function() {

               if ($('#layer_ad').css('bottom') != '-200px') {

                   $('#layer_ad').animate({'bottom':'-200px'}, 'slow');

               } else {

                   $('#layer_ad').animate({'bottom':'0px'}, 'slow');

               }

           }, 5000);

       });

// ***************************TICKETING
// function fuel_poss(){
//   var need;
//   var remain;
//
//   need = p.fm_need;
//   remain = p.fm_remain;
//   need = Number(need);
//   remain =  Number(remain);
//
//   if(need > remain){
//     document.b_btn.src=="../images/ticketing/button1.jpg"
//   }
//   else{
//     document.b_btn.src="../images/ticketing/button2.jpg"
//   }
// }


function ChangeImage2(goal, now){

    var ipath = new String();
    ipath = document.getElementById("b1").style.backgroundImage;

  if(goal <= now){
    document.getElementById("b1").style.backgroundImage="url(../images/ticketing/button1.jpg)"
  }
  else{
    document.getElementById("b1").style.backgroundImage="url(../images/ticketing/button2.jpg)"
  }
}

// *********************************
$('#trigg').click(function() {
  alert("로그인이 필요합니다");
});

$('#trigg').trigger('click');

// **************************************

function fn_changeSelected(obj) {
  var getObj = obj[obj.selectedIndex].innerHTML;
  $("#mysect").text(getObj);

  // 혹은, document.getElementById("SUBJECT").value = getObj;   등등
}

function fn_changeSelected2(obj) {
  var getObj = obj[obj.selectedIndex].innerHTML;
  $("#mysect2").text(getObj);

  // 혹은, document.getElementById("SUBJECT").value = getObj;   등등
}

function price(ob){}

$(window).load(function () {

           $('#layer_ad').css({

               'position':'fixed',

               'bottom':0,

               'right':'20px',

               'padding':'10px',

               'font-size':'12px',

               'width':'250px',

               'height':'150px',

               'border-width':'1px 1px 0 1px',

               'border-color':'#aaaaaa',

               'border-style':'solid'

           });

           setInterval(function() {

               if ($('#layer_ad').css('bottom') != '-200px') {

                   $('#layer_ad').animate({'bottom':'-200px'}, 'slow');

               } else {

                   $('#layer_ad').animate({'bottom':'0px'}, 'slow');

               }

           }, 5000);

       });

// ***************************TICKETING
function fuel_poss(){
  var need;
  var remain;

  need = p.fm_need;
  remain = p.fm_remain;
  need = Number(need);
  remain =  Number(remain);

  if(need > remain){
    document.b_btn.src=="../images/ticketing/button1.jpg"
  }
  else{
    document.b_btn.src="../images/ticketing/button2.jpg"
  }
}

var state = 0;

function ChangeImage2(){
  if(state==0){
    document.b_btn.src="/static/images/ticketing/button1.jpg"
    state=1;
  }
  else{
    document.b_btn.src="/static/images/ticketing/button2.jpg"
    state=0;
  }
}


// **************************************

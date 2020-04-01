/* 2007～2099年対応 JavaScriptカレンダー予定帳 ver. 1.5
                Copyright (c) Kumiko Maeda 2004 - 2008/09/05 */

baseDate = new Date(); //初期化  <!--引数なしで現在の日時-->

//dateを基準にdis日動かした日を返す
function moveDate( date, dis ){
  var d, m, y;
  
  d = date.getDate();
  m = date.getMonth();
  y = date.getFullYear();
  if ( ((y%4)==0 && (y%100)!=0) || (y%400)==0 ) //うるうの判定(2000～)
        monthTable[1] = 29;
  else  monthTable[1] = 28;
  
  d = d + dis;
  while( d > monthTable[m]){
    d = d - monthTable[m];
    m++;
    if( m > 11 ){
      m=0;
      y++;
      if ( ((y%4)==0 && (y%100)!=0) || (y%400)==0 ) //うるうの判定(2000～)
            monthTable[1] = 29;
      else  monthTable[1] = 28;
    }
  }
  while( d < 0 ){
    m--;
    if( m < 0 ){
      m=11;
      y--;
      if ( ((y%4)==0 && (y%100)!=0) || (y%400)==0 ) //うるうの判定(2000～)
            monthTable[1] = 29;
      else  monthTable[1] = 28;
    }
    d = d + monthTable[m];
  }
  return (new Date(y,m,d));
}



//Main関数
function showCalendar( argDate ){ //arg:引数
  var tmpDate;  //設定する日付のセルを保持しておく変数

  //引数年/月+1/日,日付テキストフォームに表示される日付
  document.formSdlCal.dateInput.value = argDate.getFullYear() + "/" +  (argDate.getMonth() + 1) + "/" + argDate.getDate();
    
  //覚えとく
  baseDate = argDate;
  //argDateの週の日曜日から表示する
  tmpDate = moveDate( argDate, -argDate.getDay() ); //-argDate.getDay():水曜なら-3で日曜日の日を指定できる
  //"今日"を記憶
  todayDate = new Date();
  
  //描画用コード開始
  docubuf = "<table border='3' cellspacing='0' " + DEFAULT + ">";
  //曜日
  /*------------------------------1行目始まり---------------------------*/
  docubuf += "<tr>";
  for(var i=0; i<7; i++){
    docubuf += "<td align='center' ";
    if(i==0)      docubuf += SUN + ">" + weekTable[i];  //SUN = "bgcolor='#f9d9c3' style='color:#ff0000;'"; //１列目日曜のセルオプション
    else if(i==6) docubuf += SAT + ">" + weekTable[i];  //SAT = "bgcolor='#f9d9c3' style='color:#0000ff;'"; //１列目土曜のセルオプション
    else          docubuf += MON + ">" + weekTable[i];  //MON = "bgcolor='#f9d9c3'"; //１列目月曜～金曜のセルオプション
    docubuf += "<\/td>";
  }
  docubuf += "<\/tr>";
  /*------------------------------1行目終わり---------------------------*/
  //日付
  /*----------------------------2~SHOWWEEK行目開始-------------------------------*/
  for(i=0; i<SHOWWEEK; i++){
    /*----------------------------2~SHOWWEEK行目1~7列目まで開始--------------------*/
    docubuf += "<tr valign='top' height='" + HEIGHT + "'>"; //HEIGHT   = "60px";  //１マスの高さ <tr height="***">
    for(var j=0; j<7; j++){                                 //WIDTH    = "120px";  //１マスの幅   <td width="***">
      /*-----------------------------<td>設定-----------------------------------------*/
      /*id用の日付の生成*/
      id_day = String(tmpDate.getFullYear()) + "-";
      
      //月
      id_month = String(tmpDate.getMonth()+1);
      if(id_month.match(/\d{2}/)) id_day += id_month + "-";
      else                        id_day += String(0) + id_month + "-";
      
      //日
      id_date = String(tmpDate.getDate());
      if(id_date.match(/\d{2}/)) id_day += id_date;
      else                       id_day += String(0) + id_date;

      /*ここまで*/
      docubuf += "<td width='" + WIDTH + "' ";
      docubuf += "class='table' ";
      docubuf += "id='" + id_day + "' ";

      //docubuf += "onclick='clicked(this);' ";
      //セル色設定
      if( tmpDate.getDate()  == todayDate.getDate()  &&
          tmpDate.getMonth() == todayDate.getMonth() &&
          tmpDate.getFullYear() == todayDate.getFullYear() )
                        docubuf += TODAY     + ">";

      else if(j==0)     docubuf += HOLIDAY   + ">";  //TODAY    = "bgcolor='#e6fff6'";
      else if(j==6)     docubuf += SATURDAY  + ">";  //HOLIDAY  = "bgcolor='#ffe6e6'";
      else              docubuf += USUALDAY  + ">";  //SATURDAY = "bgcolor='#e6e6ff'";
      /*-----------------------------<td>設定-----------------------------------------*/
      //日付表示
      //年初めは年から表示
      if( tmpDate.getDate()==1 && tmpDate.getMonth()==0 ){
        docubuf += tmpDate.getFullYear() + "/";
      }
      //最初と月初めは月から表示
      if( tmpDate.getDate()==1 || (i==0 && j==0) ){
        docubuf += tmpDate.getMonth()+1 + "/";
      }
      //普通は日だけ表示
      docubuf += tmpDate.getDate() + "<br>";

      for(key in rank){
        if(id_day == key){
          if(rank[key][1]) docubuf += "1位 " + rank[key][1][0] + " : " + rank[key][1][1] + "<br>";
          if(rank[key][2]) docubuf += "2位 " + rank[key][2][0] + " : " + rank[key][2][1] + "<br>";
        }
      }     
      //日を進める
      tmpDate = moveDate( tmpDate, 1 );
      docubuf += "<\/td>";
    }
    /*----------------------------2~SHOWWEEK行目1~7列目まで終了--------------------*/
    docubuf += "<\/tr>";
  }
  /*----------------------------2~SHOWWEEK行目終了------------------------------*/
  docubuf += "<\/table>";

  divSdlCal.innerHTML = docubuf; //id:divSdlCalのdiv区画に挿入

  
}

function clicked( argDate ) {
    let year = argDate.getFullYear();
    let month = (argDate.getMonth()+1);
    let day = argDate.getDate();
    console.log(day);
    location.href = 'http://127.0.0.1:8000/house/calendar?nextDate_year=' + encodeURIComponent(year) + "&nextDate_month=" + encodeURIComponent(month) + "&nextDate_day=" + encodeURIComponent(day);
    //表示される日付のランクを予め抜き出し
    //モーダルには日付毎の連想配列を抜き出し
}



function dumy(){
//簡単な方？
  var b = document.getElementById("board");
  
  var tr = document.createElement("tr");
  for(var i=0; i<7; i++){
    var td = document.createElement("td");
    td.align = "center";
    td.textContent = weekTable[i];
    td.style.backgroundColor = DATE_BGCOLOR;

    if(i==0)      td.style.color = SUN_STYLE; //SUN = "bgcolor='#f9d9c3' style='color:#ff0000;'"; //１列目日曜のセルオプション
    else if(i==6) td.style.color = SAT_STYLE; //SAT = "bgcolor='#f9d9c3' style='color:#0000ff;'"; //１列目土曜のセルオプション
    tr.appendChild(td);
  }
  b.appendChild(tr);
  
  //日付
  /*----------------------------2~SHOWWEEK行目開始-------------------------------*/
  for(i=0; i<SHOWWEEK; i++){
    /*----------------------------2~SHOWWEEK行目1~7列目まで開始--------------------*/
    var tr = document.createElement("tr");
    tr.vAlign = "top";
    tr.style.height = HEIGHT;

    for(var j=0; j<7; j++){                                 //WIDTH    = "120px";  //１マスの幅   <td width="***">
      /*-----------------------------<td>設定-----------------------------------------*/
      /*id用の日付の生成*/
      id_day = String(tmpDate.getFullYear());
      
      //月
      id_month = String(tmpDate.getMonth()+1);
      if(id_month.match(/\d{2}/)) id_day += id_month;
      else                        id_day += String(0) + id_month;
      
      //日付
      id_date = String(tmpDate.getDate());
      if(id_date.match(/\d{2}/)) id_day += id_date;
      else                       id_day += String(0) + id_date;

      /*ここまで*/
      var td = document.createElement("td");
      td.style.width = WIDTH;
      td.class = "table";
      td.id = id_day;

      //セル色設定
      if( tmpDate.getDate()  == todayDate.getDate()  &&
          tmpDate.getMonth() == todayDate.getMonth() )
                        td.bgcolor = TODAY;
                        //別に１年前の今日に色付けてもいいか
      else if(j==0)     td.style.backgroundColor = HOLIDAY ;  //TODAY    = "bgcolor='#e6fff6'";
      else if(j==6)     td.style.backgroundColor = SATURDAY;  //HOLIDAY  = "bgcolor='#ffe6e6'";
      else              td.style.backgroundColor = USUALDAY;  //SATURDAY = "bgcolor='#e6e6ff'";
      /*-----------------------------<td>設定----------------------------------*/
      //日付表示

      var textContent = "";
      //年初めは年から表示
      if( tmpDate.getDate()==1 && tmpDate.getMonth()==0 ){
        textContent = tmpDate.getFullYear() + "/";
      }
      //最初と月初めは月から表示
      if( tmpDate.getDate()==1 || (i==0 && j==0) ){
        textContent += tmpDate.getMonth()+1 + "/";
      }
      //普通は日だけ表示
      textContent += tmpDate.getDate() + "\n";

      td.textContent = textContent;
      //日を進める
      tmpDate = moveDate( tmpDate, 1 );
      tr.appendChild(td);
    }
    /*----------------------------2~SHOWWEEK行目1~7列目まで終了--------------------*/
    b.appendChild(tr);
  }
  /*----------------------------2~SHOWWEEK行目終了------------------------------*/
}
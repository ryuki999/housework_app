/* 2007～2099年対応 JavaScriptカレンダー予定帳 ver. 1.5
user configration file  */

SHOWWEEK = 5;   //何週表示するか

//表示スタイルオプション
WIDTH    = "120px";  //１マスの幅   <td width="***">
HEIGHT   = "60px";  //１マスの高さ <tr height="***">
DEFAULT  = "bordercolor='#cc8066' bgcolor='#fff9f6' style='font-size:12pt; color:#993333;'";
//枠線の色とフォントサイズ．デフォルトの背景色と文字色とかも<table ***>
TODAY    = "bgcolor='#e6fff6'";  //今日のセルオプション<td ***>
HOLIDAY  = "bgcolor='#ffe6e6'";  //日曜・祝日のセルオプション
SATURDAY = "bgcolor='#e6e6ff'";  //土曜のセルオプション
USUALDAY = "";  //なんでもない日のセルオプション
SUN = "bgcolor='#f9d9c3' style='color:#ff0000;'"; //１列目日曜のセルオプション
SAT = "bgcolor='#f9d9c3' style='color:#0000ff;'"; //１列目土曜のセルオプション
MON = "bgcolor='#f9d9c3'"; //１列目月曜～金曜のセルオプション

/*
TODAY    = "#e6fff6";  //今日のセルオプション<td ***>
HOLIDAY  = "#ffe6e6";  //日曜・祝日のセルオプション
SATURDAY = "#e6e6ff";  //土曜のセルオプション
DATE_BGCOLOR = "#f9d9c3";
SUN_STYLE = "#ff0000"; //１列目日曜のセルオプション
SAT_STYLE = "#0000ff"; //１列目土曜のセルオプション
*/

weekTable = new Array("日","月","火","水","木","金","土");  //1行目
monthTable= new Array(31,28,31,30,31,30,31,31,30,31,30,31); //いじるな危険

/*** スケジュール登録 notice ***
  予定はsetSchedules()に書く．
  newSchedule( 年，月, 日，"td セルオプション", "予定" );
  ・日
    －calDate( 年, 月, 週, 曜日0(sun)..6(sat))を使えば，
      第n×曜日 形式の指定も可能です．
  ・td セルオプション <td ここ>
    －指定なしは""で．
    －悪いがフォントカラーはスタイルシート("style='color:white'")で指定してくれ．
    －同じ日に複数登録したりすると効かない事があるから注意．
  ・"予定"
    －HTMLタグ使えます．
  ・祝日とあわせてMAXEVENT件までスケジュールを設定可能
*** notice スケジュール登録 ***/
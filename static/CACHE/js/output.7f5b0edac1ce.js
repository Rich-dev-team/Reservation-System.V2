;function initializeLiff(MyLiffId){liff.init({liffId:MyLiffId}).catch((err)=>{alert(err)});}
function closewindow(){if(''=='admin'){window.location.href='/softwayliving/login/'}else{liff.closeWindow()}}
function send_flexMessage(){liff.sendMessages(flex_user)
flex_user={"type":"bubble","body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":is_confirm_info,"size":"xl","weight":"bold","color":color},{"type":"box","layout":"vertical","spacing":"sm","margin":"lg","contents":[{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"預約","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":user_info.username,"flex":5,"size":"sm","color":"#666666","wrap":True}]},{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"電話","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":phone_info,"flex":5,"size":"sm","color":"#666666","wrap":True}]},{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"日期","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":data.bk_date+'-'+data.time_session+'-'+data.bk_st,"flex":5,"size":"sm","color":"#666666","wrap":True}]},{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"價位","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":'NT$ '+data.bk_price,"flex":5,"size":"sm","color":"#666666","wrap":True}]},{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"習慣","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":data.bk_habit,"flex":5,"size":"sm","color":"#666666","wrap":True}]},{"type":"box","layout":"baseline","spacing":"sm","contents":[{"type":"text","text":"備註","flex":1,"size":"sm","color":"#AAAAAA"},{"type":"text","text":data.bk_habit,"flex":5,"size":"sm","color":"#666666","wrap":True}]}]}]}}}
$(function(){initializeLiff('1653788675-gE0L04We')
if(''=='admin'){document.getElementById('close_button').innerText='返回管理者介面'}
if('0'!='0'){document.getElementById('information').innerText="訂位資訊 (候補 "+'0'+")"}})
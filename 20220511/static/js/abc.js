window.onload = function(){
    let alert_ = document.getElementById('alert_');
    let confirm_ = document.getElementById('confirm_');
    let prompt_ = document.getElementById('prompt_');
    // console.log(alert_);
    // console.log(confirm_);
    // console.log(prompt_);

    alert_.onclick = function(){ // 클릭 이벤트
        alert('alert!!');
    }

    confirm_.onclick = function(){
        if(confirm('확인 또는 취소')){
            alert('확인');
        } else{
            alert('취소');
        }
    }

    prompt_.onclick = function(){
        let plus = prompt('1 더하기 1은?', '???');
        if(plus == 2){
            window.location.href = '/basic0';
        } else{
            alert('실패!');
        }
    }
}
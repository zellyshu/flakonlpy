$(".btn-group > .btn").click(function(){
    $(".btn-group > .btn").removeClass("active");
    $(this).addClass("active");
    var selectbtnvalue = document.getElementsByClassName("btn btn-regular active")[0].value;
    document.getElementById("selectVar").value = selectbtnvalue;
    console.log(selectbtnvalue + " 선택됨")
});

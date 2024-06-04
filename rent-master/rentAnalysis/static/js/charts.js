$(document).ready(function() {
    var myChart1 = echarts.init(document.getElementById('district1'));
    myChart1.showLoading();
    var myChart2 = echarts.init(document.getElementById('district2'));
    myChart2.showLoading();
    $.ajax({
        url:"district",
        type: "GET",
        data: {},
        success: function (data) {
            myChart1.hideLoading();
            data = JSON.parse(data);
            myChart1.setOption({
                series : [
                    {
                        name: '房屋结构',
                        type: 'pie',
                        radius: '55%',
                        data:data[0]
                    }
                ]
            })
            document.getElementById("myBtn1").addEventListener("click", function(){
                document.getElementById("demo1").innerHTML = data[3];
            });
            myChart2.hideLoading();
            myChart2.setOption({
                series : [
                    {
                        name: '房屋面积',
                        type: 'pie',
                        radius: '55%',
                        data:data[1]
                    }
                ]
            })
            document.getElementById("myBtn2").addEventListener("click", function(){
                document.getElementById("demo2").innerHTML = data[2];
            });
        }
    })
});

var server_address = "http://34.77.96.109:5000/"

const params = new URLSearchParams(document.location.search);
const s = params.get("id");
/*console.log(s)
console.log(server_address+"dso/device_info?id="+s)
console.log($.getJSON(server_address+"dso/device_info?id="+s))*/
var pulsado = 0;


var get_device_info = function(){
    $.getJSON(server_address+"dso/device_info?id="+s, function( data ){
        $.each(data, function(key, elem){

            $(".device_info").append(
                "Dispositivo: " + elem.device_id + " - " + elem.status + " - (" + elem.location + ")"
            );
            //console.log($(".device_info"))

        });
    });
}

var get_current_sensor_data_table = function() {
    if (pulsado > 0){

        if (document.getElementById("end").value != "" && document.getElementById("start").value != ""){

            var start = new Date(document.getElementById("start").value);
            var start_mili = start.getTime()/1000;
            var end = new Date(document.getElementById("end").value);
            var end_mili = end.getTime()/1000;
            if (start_mili <= end_mili){
                console.log("Start: "+start_mili)
                console.log("End: "+end_mili)
                $.getJSON(server_address+"dso/measurements_date?id="+s+"&start="+start_mili+"&end="+end_mili, function( data ) {
                    $( ".sensor_measures" ).html("");
                    $.each(data, function(key, elem){
                        var date = new Date(elem.time_stamp*1000);
                        var converted_date = date.getDate()+
                        "/"+(date.getMonth()+1)+
                        "/"+date.getFullYear()+
                        " "+date.getHours()+
                        ":"+date.getMinutes()+
                        ":"+date.getSeconds();

                        $(".sensor_measures").append('<tr>' +
                        '<td align="center" style="dislay: none;">' + converted_date + '</td>'+
                        '<td align="center" style="dislay: none;">' + elem.temperature + " C" + '</td>'+
                        '<td align="center" style="dislay: none;">' + elem.humidity + " %" + '</td>'+'</tr>');
                        //console.log($(".sensor_measures"))
                    });
                });
            }else{
                $( ".sensor_measures" ).html("");
            }
        }else{
            $( ".sensor_measures" ).html("");
        }
    }else{
        $.getJSON(server_address+"dso/measurements?id="+s, function( data ) {
        $( ".sensor_measures" ).html("");
        $.each(data, function(key, elem){
            var date = new Date(elem.time_stamp*1000);
            var converted_date = date.getDate()+
            "/"+(date.getMonth()+1)+
            "/"+date.getFullYear()+
            " "+date.getHours()+
            ":"+date.getMinutes()+
            ":"+date.getSeconds();

            $(".sensor_measures").append('<tr>' +
            '<td align="center" style="dislay: none;">' + converted_date + '</td>'+
            '<td align="center" style="dislay: none;">' + elem.temperature + " C" + '</td>'+
            '<td align="center" style="dislay: none;">' + elem.humidity + " %" + '</td>'+'</tr>');
            //console.log($(".sensor_measures"))
        });
    });
    }
}

function volver(){
	window.location="index.html";
	console.log("Pulsado")
}

function filtrar(){
    pulsado = pulsado + 1;
    get_current_sensor_data_table()
}

get_device_info()
get_current_sensor_data_table()
//setInterval(get_current_sensor_data_table,100)
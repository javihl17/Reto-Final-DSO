/*
 * Javascript file to implement client side usability for 
 * Operating Systems Desing exercises.
 */
var server_address = "http://34.77.96.109:5000/"

var get_device_list_table = function(){
    $.getJSON(server_address+"dso/devices/", function( data ) {
        $.each(data, function(key, elem){
            var date = new Date(elem.time_stamp*1000);
            var converted_date = date.getDate()+
            "/"+(date.getMonth()+1)+
            "/"+date.getFullYear()+
            " "+date.getHours()+
            ":"+date.getMinutes()+
            ":"+date.getSeconds();

            $(".device_list").append(
            '<tr>' +'<td align="center" style="dislay: none;">' + elem.device_id + '</td>'+
            '<td align="center" style="dislay: none;">' + elem.status + '</td>'+
            '<td align="center" style="dislay: none;">' + elem.location + '</td>'+
            '<td align="center" style="dislay: none;">' + converted_date + '</td>'+
            '<td>'+'<input type="button" class="medidas" onclick="medidas(\'' + elem.device_id + '\')" value="Medidas">'+'</td>'+'</tr>');
            console.log($(".device_list"))
        });
    });
}

var get_device_list = function(){
	$.getJSON(server_address+"dso/devices/", function( data ) {
	    $( ".device_list" ).html("");
	    $.each(data, function(key,elem) {
		    $( "<div/>" ).appendTo( ".device_list").append( "Device Id: " + elem.device_id)});
	});
}

function medidas(id){
    console.log("Pulsado")
	console.log(id)
	window.location.href="medidas.html?id="+id;
}

/*setInterval(get_current_sensor_data_table,100)*/
get_device_list_table()
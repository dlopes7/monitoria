function chart(){


    var app_id = $( "#sel_application option:selected" ).val();
    var metric_id = $( "#sel_metric option:selected" ).val();
    var time_from = $('#date_from').data("DateTimePicker").date().format("D/M/YYYY HH:mm:ss");
    var time_to = $('#date_to').data("DateTimePicker").date().format("D/M/YYYY HH:mm:ss");
    //var url = 'www.extra.com.br';


    queue()
    .defer(d3.json, "/json_chart/?app_id=" + app_id + "&metric=" + metric_id + "&time_from="+time_from + "&time_to=" + time_to)
    .await(makeGraphs);
}

$( document ).ready(function() {
    $( "#btn_chart" ).click(function() {
        chart();
    });
});


function makeGraphs(error, testes) {

    var num_testes = testes.length;

    if (num_testes == 0){
            alert(testes.length + ' testes encontrados');
    }

    testes.forEach(function(d) {

        var js_date =  new Date(d['fields']['created_date']);
	    js_date.setTime( js_date.getTime() + js_date.getTimezoneOffset()*60*1000 );
		d['fields']['created_date'] = js_date;

    });

    var ndx = crossfilter(testes);
    var all = ndx.groupAll();

    var dateDim = ndx.dimension(function(d) {
        return d['fields']['created_date'];
    });

    var minDate = dateDim.bottom(1)[0]['fields']['created_date'];
    var maxDate = dateDim.top(1)[0]['fields']['created_date'];

    var dateGroup = dateDim.group().reduceSum(function(d) {
        console.log(d['fields']['wpt_firstView_bytesIn']);
        return d['fields']['wpt_firstView_bytesIn'];

    });

    var timeChart = dc.lineChart("#time-chart");
	timeChart
		.width($(document).width() * 0.70)
		.height(320)
		.brushOn(true)
		.margins({top: 10, right: 150, bottom: 30, left: 100})
		.dimension(dateDim)
		.group(dateGroup)
		.x(d3.time.scale().domain([minDate,maxDate]))
		.elasticY(true)
		.xAxisLabel("Grafico")
		.xAxis().ticks(num_testes);

    dc.renderAll();






}
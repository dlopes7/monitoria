function chart(){

    var app_id = $( "#sel_application option:selected" ).val();
    var metric_id = $( "#sel_metric option:selected" ).val();
    var time_from = $('#date_from').data("DateTimePicker").date().format("D/M/YYYY HH:mm:ss");
    var time_to = $('#date_to').data("DateTimePicker").date().format("D/M/YYYY HH:mm:ss");

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
    var metric = $( "#sel_metric option:selected" ).val();
    var metric_name = $( "#sel_metric option:selected" ).text();
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

    var tudoDim = ndx.dimension(function(d) {
        return d;
    });

    var minDate = dateDim.bottom(1)[0]['fields']['created_date'];
    var maxDate = dateDim.top(1)[0]['fields']['created_date'];

    var dateGroup = dateDim.group().reduceSum(function(d) {
        return d['fields'][metric];

    });

    var timeChart = dc.lineChart("#time-chart");
	timeChart
		.width($(document).width() * 0.70)
		.height(320)
		.brushOn(true)
		.margins({top: 20, right: 150, bottom: 30, left: 100})
		.dimension(dateDim)
		.group(dateGroup)
		.x(d3.time.scale().domain([minDate,maxDate]))
		.elasticY(true)
		.yAxisLabel(metric_name)
		.xAxisLabel("Horario")
		.xAxis().ticks(24);

    var tempoFormat = d3.time.format("%d/%m/%Y %H:%M:%S");
    var dataFormat = d3.time.format("%d/%m/%Y");

	var testsTable = dc.dataTable('.tests-table');
    testsTable
	    .dimension(tudoDim)
	    .group(function (d) {
            return dataFormat(d['fields']['created_date']);
        })
        .size(1000)
	    .columns([
	        {
	           label:'Horario',
	           format: function(d){
	            return tempoFormat(d['fields']['created_date']);
	           }
	        },
	        {
	           label:'Url',
	           format: function(d){
	            return d['fields']['url'];
	           }
	        },
	        {
	           label:metric_name,
	           format: function(d){
	            return d['fields'][metric];
	           }
	        }
        ])
        .showGroups(false)
        .sortBy(function (d) {
            return d['fields']['created_date'];
        })
    dc.renderAll();






}